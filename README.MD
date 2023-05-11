<!-- Improved compatibility of back to top link: See: https://github.com/saladball/Abuse_autopilot/pull/73 -->

<a name="readme-top"></a>

<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
[![Discord][discord-shield]][discord-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center">Daily malware distribution site</h3>

  <p align="center">
    데일리 악성코드 유포지 자동 추출기
    <br />
    <a href="https://github.com/saladball/Abuse_autopilot"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/saladball/Abuse_autopilot">View Demo</a>
    ·
    <a href="https://github.com/saladball/Abuse_autopilot/issues">Report Bug</a>
    ·
    <a href="https://github.com/saladball/Abuse_autopilot/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#notice">Notice</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#references">References</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

일일 악성코드 유포지 확인을 위해 만들었습니다.
이 프로젝트는 A3Security 업무용으로 참고하기 위해 제작되었습니다.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

Abuse_autopilot_beta.zip을 다운받아 주세요.

### Prerequisites

- pip
  ```sh
  pip install geoip2 datetime pandas
  ```

### Notice

<b>오남용 금지</b>

- 해당 파일 사용 시 추후 문제되거나 잘못되면 작성자와 일절 관계없습니다.
- 압축폴더 안에있는 GeoLite2-County.mmdb, spam_email_list.txt 파일은 실행파일에 종속되어있습니다. 지우면 실행되지 않습니다.
- 반드시 중복체크.xlsx 파일이 있는곳에서 사용해주세요.
- 악성 email 도 2개 중복체크.xlsx 파일에 추가되지만 이메일 제목은 없습니다. 참고해주세요.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE -->

## Usage

1. 중복체크.xlsx 파일이 있는곳에서 실행해주세요.
2. Abuse_autopilot_beta.zip 압축 폴더 압축해제 후 Abuse_autopilot_beta.exe 파일 실행
3. 현재 폴더에 {오늘 날짜}\_재정정보원.csv 파일 생성되어 있을겁니다.
4. 실행 후 추가된 모든 데이터(악성코드유포지, 악성 email, 추가된 날짜)는 <b>중복체크.xlsx</b> 에 자동으로 추가됩니다.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## License

MIT 라이선스에 따라 배포됩니다. 자세한 내용은 `LICENSE.txt`를 참조해주세요.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

An Hyukjin - [telegram](https://t.me/debu_man) - silverfast8@yahoo.com

Project Link: [https://github.com/saladball/Abuse_autopilot](https://github.com/saladball/Abuse_autopilot)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->

## References

- [urlhaus API](https://urlhaus.abuse.ch/api/)
- [maxmind GeoIP](https://www.maxmind.com/en/accounts/856267/geoip/downloads)
- [stopforumspam](https://www.stopforumspam.com/downloads)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/saladball/Abuse_autopilot.svg?style=for-the-badge
[contributors-url]: https://github.com/saladball/Abuse_autopilot/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/saladball/Abuse_autopilot.svg?style=for-the-badge
[forks-url]: https://github.com/saladball/Abuse_autopilot/network/members
[stars-shield]: https://img.shields.io/github/stars/saladball/Abuse_autopilot.svg?style=for-the-badge
[stars-url]: https://github.com/saladball/Abuse_autopilot/stargazers
[issues-shield]: https://img.shields.io/github/issues/saladball/Abuse_autopilot.svg?style=for-the-badge
[issues-url]: https://github.com/saladball/Abuse_autopilot/issues
[license-shield]: https://img.shields.io/github/license/saladball/Abuse_autopilot.svg?style=for-the-badge
[license-url]: https://github.com/saladball/Abuse_autopilot/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/hyukjin-an-429858248
[discord-shield]: https://img.shields.io/discord/1099579874399768576?style=for-the-badge&logo=discord
[discord-url]: https://discord.com/channels/1099579874399768576/1099580046651441214
