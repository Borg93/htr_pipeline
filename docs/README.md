---
hide:
  - navigation
---

<img src="images/riks.png" width="20%" height="20%" align="right" />

# **htr**

The HTR (Handwritten Text Recognition) Pipeline is a package that takes an image as input, runs preprocessing algorithms, feeds it into an inference engine, and outputs the results in either XML or JSON format. The inference engine can use models from a variety of third-party libraries such as OpenMMLab, Hugging Face, or others.

![Test Python 🐍 package ](https://github.com/Riksarkivet/htr/actions/workflows/tests.yml/badge.svg)
[![Publish Python 🐍 distributions 📦 to PyPI](https://github.com/Riksarkivet/htr/actions/workflows/release.yml/badge.svg)](https://github.com/Riksarkivet/htr/actions/workflows/release.yml)
[![Automatic generating docs for 📦](https://github.com/Riksarkivet/htr/actions/workflows/docs.yml/badge.svg)](https://github.com/Riksarkivet/htr/actions/workflows/docs.yml)
[![PyPI - License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/Riksarkivet/htr/blob/master/LICENSE)
[![PyPI - Python](https://img.shields.io/badge/python-3.7%20|%203.8%20|%203.9-blue.svg)](https://pypi.org/project/htr/)

## **Installation**

Installation can be done using [pypi](https://pypi.org/project/htr/):

```
pip install htr
```

## Key Features

- **Step-by-Step Pipeline:** The HTR pipeline can be executed step-by-step, allowing you to visualize and analyze the results at each stage.
- **Model Agnostic:** The inference engine is framework-agnostic and can use any model that conforms to a specified interface.
- **Postprocessing Steps:** Each inference step includes postprocessing steps to enhance the model outputs.
- **Visualization:** Each step can be visualized for easier analysis and debugging.
- **Easy Model Swapping:** You can easily swap out the models at any stage of the pipeline to experiment and compare results.

## Getting Started

### Installation

*Provide instructions for how to install your package. This might involve running pip install, cloning a GitHub repository, etc.*

### Usage

*Provide instructions for how to use your package. This might involve initializing the HTREngine, loading models, running the pipeline, etc.*

## Contributing

We welcome contributions! Please see `CONTRIBUTING.md` for details on how to contribute.

## Testing

*Provide instructions for how to run the test suite.*

## Code Structure

*Optionally provide an overview of the code structure and key classes.*

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

If you have any questions, please contact *Your Contact Information*.