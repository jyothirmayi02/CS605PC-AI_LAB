{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNQap1fFBZQ3/kPvs0iIJN8",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/jyothirmayi02/CS605PC-AI_LAB/blob/main/numpy.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "9DCZhLnnkQ8d"
      },
      "outputs": [],
      "source": [
        "#numpy basics\n",
        "import numpy as np\n",
        "\n",
        "a = np.array([1, 2, 3])   # Create a rank 1 array\n",
        "print(type(a))\n",
        "print(a.shape)            # Prints \"(3,)\"\n",
        "print(a[0], a[1], a[2])   # Prints \"1 2 3\"\n",
        "a[0] = 5                  # Change an element of the array\n",
        "print(a)                  # Prints \"[5, 2, 3]\"\n",
        "b = np.array([[1,2,3],[4,5,6]])    # Create a rank 2 array\n",
        "print(b.shape)                     # Prints \"(2, 3)\"\n",
        "print(b[0, 0], b[0, 1], b[1, 0])   # Prints \"1 2 4\"\n",
        "\n"
      ]
    }
  ]
}