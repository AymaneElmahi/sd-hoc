<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->

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

[![Author](https://img.shields.io/badge/author-@AymaneElmahi-blue)](https://github.com/AymaneElmahi)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Paper](https://img.shields.io/badge/paper-here-svg)](<https://github.com/cruiseresearchgroup/SD-HOC-Seasonal-Decomposition-Algorithm-for-Mining-Lagged-Time-Series/blob/master/paper/AusDM2017_IrvanAriefAng_(CCIS).pdf>)

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/AymaneElmahi/sd-hoc">
    <img src="sdhoc_logo.png" alt="Logo" width="80" height="80">
  </a> 

<h3 align="center">Implementation Of SD-HOC Algorithm </h3>

  <p align="center">
    This project implements the SD-HOC algorithm for predicting the people count in a room solely using CO2 data, utilizing machine learning and time series techniques for accurate real-time occupancy estimation and efficient spatial management. The algorithm's non-intrusive approach makes it suitable for various applications in facilities management and smart building systems.
    <br />
    <a href="https://github.com/AymaneElmahi/sd-hoc"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <!-- <a href="https://github.com/AymaneElmahi/sd-hoc">View Demo</a> -->
    <a href="https://github.com/AymaneElmahi/sd-hoc/issues">Report Bug</a>
    <!-- ·
    <a href="https://github.com/AymaneElmahi/sd-hoc/issues">Request Feature</a> -->
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <!-- <li><a href="#roadmap">Roadmap</a></li> -->
    <!-- <li><a href="#contributing">Contributing</a></li> -->
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <!-- <li><a href="#acknowledgments">Acknowledgments</a></li> -->
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

![Product Name Screen Shot][product-screenshot]

This project is an implementation of the SD-HOC (Seasonal Decomposition Algorithm for Mining Lagged Time Series) algorithm, designed to accurately predict the people count in a room using solely the CO2 data obtained from that very room. The SD-HOC algorithm leverages the relationship between human presence and CO2 levels, utilizing the principle that as humans occupy an enclosed space, they release carbon dioxide through respiration, leading to a discernible increase in CO2 concentration.

To achieve precise people count predictions, this implementation combines machine learning and time series techniques. Machine learning models are employed to learn complex patterns and dependencies present in the CO2 data, allowing for robust predictions even in dynamic environments.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

<!-- python, jupyter, tensorflow, pandas -->

<!-- [![Python](https://img.shields.io/badge/python-3.9.0-blue)](https://www.python.org/downloads/release/python-390/)  
[![Jupyter](https://img.shields.io/badge/jupyter-6.1.4-orange)](https://jupyter.org/)  
[![Tensorflow](https://img.shields.io/badge/tensorflow-2.4.0-red)](https://www.tensorflow.org/)  
[![Pandas](https://img.shields.io/badge/pandas-1.2.0-yellow)](https://pandas.pydata.org/) -->

<img align="left" alt="Python" width="50px" style="padding-right:10px;" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-plain.svg" />
<img align="left" alt="Tensorflow" width="50px" style="padding-right:10px;" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tensorflow/tensorflow-original.svg" />        
<img align="left" alt="Pandas" width="50px" style="padding-right:10px;" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original-wordmark.svg" />
<img align="left" alt="Jupyter" width="50px" style="padding-right:10px;" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jupyter/jupyter-original-wordmark.svg"/>

<br/><br/>



<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

### Prerequisites

To install all the required libraries for this project, run the following command:

```sh
pip install -r requirements.txt
```

### Installation

```sh
git clone https://github.com/AymaneElmahi/sd-hoc.git
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## Usage

This project may be useful for anyone looking to implement the SD-HOC algorithm for occupancy estimation in their own applications. The algorithm's non-intrusive approach makes it suitable for various applications in facilities management and smart building systems.

_For more details about the algorithm in itself, please refer to the [paper](https://github.com/cruiseresearchgroup/SD-HOC-Seasonal-Decomposition-Algorithm-for-Mining-Lagged-Time-Series/blob/master/paper/AusDM2017_IrvanAriefAng_(CCIS).pdf)_

To run the project, you can run the `main.py` file in the `src` directory, it requires three arguments:

- `JSON_FILES` : The path to the json_files that contains the people count data. (Take a look at the function create_final_df in the file `utils.py` to see how the json files should be structured)
- `CO2_DATA` : The path to the co2_file.csv that contains the CO2 data. (Take a look at the function create_final_df in the file `utils.py` to see how the co2 files should be structured)
- `COMMAND` : The command to run, it can be either `train` or `run`.

Here is an example of how to run the project:

```sh
python src/main.py ./data/json_files ./data/co2_file.csv train
```
> `Note`: This section needs more explanation on what type of data is expected, the name of the columns, etc...  
> -------> You can take a look at the `utils.py` file to see how the data should be structured.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->

## The code is divided into 2 main parts:

1. `Data Visualization` : This part is dedicated to the visualization of the data, and the analysis of the different features.

2. `Algorithm Implementation` : This part is dedicated to the implementation of the SD-HOC algorithm, and the training of the machine learning models.

I have to note that I didn't go through the whole implementation of the algorithm, as I only implemented the parts that I found relevant to my project. I also added some of my own ideas to the algorithm, such as the use of a KNN classifier to predict the occupancy of the room at a given time.
Here is the flowchart of the algorithm I implemented:

![Flowchart][flowchart]

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

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

Aymane EL MAHI : [Message me on LinkedIn](https://www.linkedin.com/in/aymane-elmahi)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->

<!-- ## Acknowledgments

- []()
- []()
- []() -->
<!--
<p align="right">(<a href="#readme-top">back to top</a>)</p> -->

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/AymaneElmahi/sd-hoc.svg?style=for-the-badge
[contributors-url]: https://github.com/AymaneElmahi/sd-hoc/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/AymaneElmahi/sd-hoc.svg?style=for-the-badge
[forks-url]: https://github.com/AymaneElmahi/sd-hoc/network/members
[stars-shield]: https://img.shields.io/github/stars/AymaneElmahi/sd-hoc.svg?style=for-the-badge
[stars-url]: https://github.com/AymaneElmahi/sd-hoc/stargazers
[issues-shield]: https://img.shields.io/github/issues/AymaneElmahi/sd-hoc.svg?style=for-the-badge
[issues-url]: https://github.com/AymaneElmahi/sd-hoc/issues
[license-shield]: https://img.shields.io/github/license/AymaneElmahi/sd-hoc.svg?style=for-the-badge
[license-url]: https://github.com/AymaneElmahi/sd-hoc/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/aymane-elmahi
[product-screenshot]: images/about_the_project_screenshot.png
[Flowchart]: images/flowchart.png
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
