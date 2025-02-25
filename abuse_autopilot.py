import csv
import requests
from urllib.parse import urlparse
import re
import socket
from socket import getaddrinfo
import geoip2.database
import datetime
import pandas as pd
import random
from modules.County_Codes import country_code_to_korean

# 국가 코드를 한국어 국가 이름으로 변환하는 함수
def get_korean_country_name(country_code):
    return country_code_to_korean.get(country_code, '미국')

def get_country(reader, ip_address):
    try:
        response = reader.country(ip_address)
        return response.country.iso_code
    except:
        return 'US'

# spam_email_list.txt 파일에서 이메일 주소를 읽어옵니다.
with open("spam_email_list.txt", "r") as file:
    email_addresses = file.readlines()

# 이메일 주소를 랜덤하게 2개 선택합니다.
random_emails = random.sample(email_addresses, 2)

# 다운로드 URL 지정
url = "https://urlhaus.abuse.ch/downloads/text/"

# 파일 다운로드
response = requests.get(url)
text_data = response.text.splitlines()

# 텍스트 데이터를 CSV 형식으로 변환
reader = csv.reader(text_data)

# 3열에서 URL 추출 (3열이 없거나 빈 행을 무시)
urls = [row[0] for row in reader if len(row) > 0 and row[0]]

# URL에서 "http://" 또는 "https://"부터 첫 번째 "/"까지의 값을 추출
domains = [urlparse(url).netloc.split(':')[0] for url in urls]

# 중복 값 제거
unique_domains = list(set(domains))

# IP 주소와 도메인 이름 구분
ip_regex = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
domain_name_regex = re.compile(r'(?:(?:[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?\.)+[A-Za-z]{2,6})')
ips = [domain for domain in unique_domains if ip_regex.fullmatch(domain)]
domains = [domain for domain in unique_domains if domain_name_regex.fullmatch(domain)]

# 중복체크.xlsx 파일과 비교하기 위해 일단 중복 값 제거된 IP 주소와 도메인 이름을 하나의 리스트로 결합
check_df = pd.read_excel("중복체크.xlsx", header=None, engine='openpyxl')
check_list = check_df.iloc[:, 0].tolist()

# 중복되지 않은 IP 주소와 도메인 이름 저장
unique_ips = [ip for ip in ips if ip not in check_list]
unique_domains = [domain for domain in domains if domain not in check_list]

# 요청된 개수만큼 IP 주소와 도메인 이름 선택
selected_ips = unique_ips[:198]
selected_domains = unique_domains[:2] if len(unique_domains) >= 2 else unique_domains

# 선택된 IP 주소와 도메인 이름을 하나의 리스트로 결합
final_data = selected_ips + selected_domains

# GeoLite2 데이터베이스 읽기
reader = geoip2.database.Reader('GeoLite2-Country.mmdb')

# 국가 코드가 KR인 것들을 제거
final_data = [domain for domain in final_data if get_country(reader, domain) != "KR"]

# 오늘 날짜 기반으로 파일명 설정
today = datetime.datetime.today().strftime('%y%m%d')
filename = f"{today}_악성IP&URL.xlsx"

# 데이터를 DataFrame으로 변환
data = []
for i, domain in enumerate(final_data):
    if ip_regex.fullmatch(domain):
        country_code = get_country(reader, domain)
    else:
        try:
            ip_address = getaddrinfo(domain, None)[0][4][0]
            country_code = get_country(reader, ip_address)
        except (socket.gaierror, IndexError) as e:
            print(f"Domain resolution error for {domain}: {e}")
            country_code = 'US'  # 기본값 설정
    
    country_name = get_korean_country_name(country_code)
    data.append(['' if i < 198 else domain, domain if i < 198 else '', country_name])

df = pd.DataFrame(data, columns=['URL', '공격 IP', '공격국가'])

# Excel 파일로 저장
df.to_excel(filename, index=False, engine='openpyxl', sheet_name=f"{today}_악성IP&URL")

# GeoLite2 데이터베이스 닫기
reader.close()

# 중복체크.xlsx 업데이트
last_row = check_df.iloc[:, 0].last_valid_index()
for index, value in enumerate(final_data):
    check_df.at[last_row + 1 + index, 0] = value

for email in random_emails:
    email = email.strip()
    if email not in check_list:
        last_row = check_df.iloc[:, 0].last_valid_index()
        check_df.at[last_row + 1, 0] = email
        check_df.at[last_row + 1, 1] = datetime.datetime.today().strftime('%Y-%m-%d')

check_df.to_excel("중복체크.xlsx", index=False, header=None, engine='openpyxl')
