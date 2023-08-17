<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/janskn/poker-calculator">
    <img src="src/frontend/images/logo.jpg" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Poker Calculator</h3>

  <p align="center">
    A calculator to determine your card rank odds
    <br />
    <a href="https://github.com/janskn/poker-calculator"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/janskn/poker-calculator/issues">Report Bug</a>
    ·
    <a href="https://github.com/janskn/poker-calculator/issues">Request Feature</a>
  </p>
</div>



<!-- ABOUT THE PROJECT -->
## About The Project

This poker calculator for Texas Hold'em determines the odds of each card rank for every stage (Flop, Turn, River).

If there is an occurance of a rank that is covered by a higher rank, it will not be counted. 
Example: Three-of-a-Kind is also a Pair, but in this case, the Pair is not considered.  

Royal Flush is not listed since it is the highest Straight Flush and only has 4 possibilities.

The frontend of this project was made with HTML and Javascript, the calculations are done with Python. Data is exchanged with REST-Api.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

This project was build with

* HTML
* JavaScript
* Python
* FetchAPI/FastAPI

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Installation

_Follow these steps to run the project._

1. Clone the repo
   ```sh
   git clone https://github.com/janskn/poker-calculator.git
   ```
2. Install FastAPI
   ```sh
   pip install fastapi
   ```
3. Install Uvicorn
   ```sh
   pip install uvicorn
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Open the index.html file.
Run Uvicorn from the path of the api.py file
```sh
   uvicorn api:app --reload
```

Simply drag a card into the hand cards or community cards area. 
Once you selected 2 hand cards and at least 3 community cards, the probabilities get displayed.
Remove a card by clicking it.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Jan Skowron - jan.a.skowron@gmail.com

Project Link: [https://github.com/janskn/poker-calculator](https://github.com/janskn/poker-calculator)

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
