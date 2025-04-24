# Conversia unei expresii regulate în automat finit determinist (DFA)

## 📖 Cuprins

- [📝 Descriere](#-descriere)
- [🗃️ Structura proiectului](#️-structura-proiectului)
- [💻 Rulare](#-rulare)
- [🤔 Decizii de implementare](#-decizii-de-implementare)

---

## 📝 Descriere

Acest proiect implementează un convertor de expresii regulate într-un automat finit determinist (DFA) și testarea acceptării cuvintelor fără a utiliza biblioteci externe pentru manipularea expresiilor regulate sau a automatelor.

Funcționalitățile principale includ:

- Parsarea și transformarea în formă postfixată a unei expresii regulate.
- Construirea unui λ-NFA dintr-o expresie regulată în formă postfixată.
- Conversia unui λ-NFA în DFA.
- Verificarea acceptării cuvintelor de un DFA.

---

## 🗃️ Structura proiectului

```
project-root/
├── main.py
├── regex_utils.py
├── postfix_to_lambda_nfa.py
├── lambda_nfa_utils.py
├── lambda_nfa_to_dfa.py
├── dfa_string_acceptance.py
├── input.json
└── results.txt
```

### Descrierea fișierelor

- **`main.py`**: citește inputul din `input.json` și scrie rezultatele testării cuvintelor în `results.txt`
- **`regex_utils.py`**: modul pentru parsarea unei expresii regulată și conversia ei în formă postfixată folosind algoritmul *shunting yard*
- **`postfix_to_lambda_nfa.py`**: modul pentru transformarea unei expresii regulate în λ-NFA folosind *Algoritmul lui Thompson*
- **`lambda_nfa_utils.py`**: modul pentru transformarea fiecărei operații într-un λ-NFA
   - **`|`** (reuniune)
   - **`·`** (concatenare)
   - **`*`** (stelare)
   - **`+`** (stelare cu minim o apariție)
   - **`?`** (apariție opțională)
- **`lambda_nfa_to_dfa.py`**: modul pentru transformarea unui λ-NFA în DFA folosind *subset construction*
- **`dfa_string_acceptance.py`**: modul pentru verificarea acceptării unui cuvând de un DFA
- **`input.json`**: 20 de expresii regulate, fiecare cu cuvinte pentru testat și rezultatele așteptate
- **`results.txt`**: rezultatele testării tuturor cuvintelor

---

## 💻 Rulare

1. clonare repository:
   ```
   git clone https://github.com/biancalautaru/Regex-to-DFA
   ```
2. rulare main:
   ```
   python3 main.py
   ```

---

## 🤔 Decizii de implementare

### Transformarea expresiei regulate în formă postfixată

- Am introdus **`·`** între literali pentru a ușura transformarea.
- Am folosit algoritmul *shunting yard* pentru a converti expresia utilizând o stivă.

### Transformarea expresiei regulate în formă postfixată în λ-NFA

- Am folosit *Algoritmul lui Thompson* pentru a construi un λ-NFA utilizând o stivă.
- Am scris funcții separate pentru transformarea fiecărei „bucăți” din expresia regulată.

### Transformarea λ-NFA în DFA

- Am găsit lambda-închiderile pentru fiecare stare folosind un algoritm DFS. 
- Am folosit o coadă pentru a procesa eficient și ordonat toate stările.

### Verificarea acceptării cuvintelor de DFA

- Începând cu starea inițială, am verificat pentru fiecare literă a cuvântului dacă se poate trece într-o altă stare cu acea literă.
- Am verificat dacă atunci când s-a terminat cuvântul, s-a ajuns într-o stare finală.
