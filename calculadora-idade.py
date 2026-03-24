{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOxp/cWE22/T0KFudTky2XK",
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
        "<a href=\"https://colab.research.google.com/github/MatheusNikolayRodriguesdosSantos1/idade-calculo.py/blob/main/calculadora-idade.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "6OSwBdK20hY1"
      },
      "outputs": [],
      "source": [
        "# Sistema básico em Python\n",
        "# Autor: Matheus Nikolay\n",
        "\n",
        "def mostrar_menu():\n",
        "    print(\"\\n===== MENU =====\")\n",
        "    print(\"1 - Calcular ano de nascimento\")\n",
        "    print(\"2 - Somar dois números\")\n",
        "    print(\"3 - Mostrar dados do usuário\")\n",
        "    print(\"0 - Sair\")\n",
        "\n",
        "def calcular_ano_nascimento():\n",
        "    ano_nasc = int(input(\"Digite o ano de nascimento: \"))\n",
        "    ano_atual = int(input(\"Digite o ano atual: \"))\n",
        "    idade = ano_atual - ano_nasc\n",
        "    print(f\"Você tem {idade} anos\")\n",
        "\n",
        "def somar_numeros():\n",
        "    num1 = int(input(\"Digite o primeiro número: \"))\n",
        "    num2 = int(input(\"Digite o segundo número: \"))\n",
        "    soma = num1 + num2\n",
        "    print(f\"A soma é: {soma}\")\n",
        "\n",
        "def dados_usuario():\n",
        "    nome = input(\"Digite seu nome: \")\n",
        "    idade = int(input(\"Digite sua idade: \"))\n",
        "    altura = float(input(\"Digite sua altura: \"))\n",
        "\n",
        "    print(f\"\\nNome: {nome}\")\n",
        "    print(f\"Idade: {idade}\")\n",
        "    print(f\"Altura: {altura:.2f}\")\n",
        "\n",
        "# Programa principal\n",
        "while True:\n",
        "    mostrar_menu()\n",
        "    opcao = input(\"Escolha uma opção: \")\n",
        "\n",
        "    if opcao == \"1\":\n",
        "        calcular_ano_nascimento()\n",
        "    elif opcao == \"2\":\n",
        "        somar_numeros()\n",
        "    elif opcao == \"3\":\n",
        "        dados_usuario()\n",
        "    elif opcao == \"0\":\n",
        "        print(\"Encerrando o programa...\")\n",
        "        break\n",
        "    else:\n",
        "        print(\"Opção inválida!\")"
      ]
    }
  ]
}