# iACP-RF: Accurately Predicting AntiCancer Peptide using ensemble of heterogeneously Trained Classifiers

### [1]. Read File:
All the datasets file are in `FASTA` format which can be with `.txt` or `.fasta` extension. E.g. `anyName.txt` or  `anyName.fasta`. Please know more about the FASTA file format [by clicking here!](https://en.wikipedia.org/wiki/FASTA_format).

```
>sp|A8MTJ3|GNAT3_HUMAN Guanine nucleotide-binding protein G(t) subunit alpha-3 OS=Homo sapiens OX=9606 GN=GNAT3 PE=2 SV=2
MGSGISSESKESAKRSKELEKKLQEDAERDARTVKLLLLGAGESGKSTIVKQMKIIHKNGYSEQECMEFKAVIYSNTLQSILAIVKAMTTLGIDYVNPRSAEDQRQLYAMANTLEDGGMTPQLAEVIKRLWRDPGIQACFERASEYQLNDSAAYYLNDLDRITASGYVPNEQDVLHSRVKTTGIIETQFSFKDLHFRMFDVGGQRSERKKWIHCFEGVTCIIFCAALSAYDMVLVEDEEVNRMHESLHLFNSICNHKYFSTTSIVLFLNKKDIFQEKVTKVHLSICFPEYTGPNTFEDAGNYIKNQFLDLNLKKEDKEIYSHMTCATDTQNVKFVFDAVTDIIIKENLKDCGLF
>sp|B2RU33|POTEC_HUMAN POTE ankyrin domain family member C OS=Homo sapiens OX=9606 GN=POTEC PE=2 SV=2
MVTEVCSMPAASAVKKPFDLRSKMGKWFHHRFPCCKGSGKSNMGTSGDHDDSFMKMLRSKMGKCCHHCFPCCRGSGTSNVGTSGDHDNSFMKTLRSKMGKWCCHCFPCCRGSGKSNVGAWGDYDDSAFMEPRYHVRREDLDKLHRAAWWGKVPRKDLIVMLRDTDMNKRDKQKRTALHLASANGNSEVVQLLLDRRCQLNVLDNKKRTALIKAVQCQEDECVLMLLEHGADQNIPDEYGNTTLHYAVHNEDKLMAKALLLYGADIESKNKCGLTPLLLGVHEQKQQVVKFLIKKKANLNALDRYGRTALILAVCCGSASIVNLLLEQNVDVSSQDLSGQTAREYAVSSHHHVICELLSDYKEKQMLKISSENSNPEQDLKLTSEEESQRLKVSENSQPEKMSQEPEINKDCDREVEEEIKKHGSNPVGLPENLTNGASAGNGDDGLIPQRRSRKPENQQFPDTENEEYHSDEQNDTRKQLSEEQNTGISQDEILTNKQKQIEVAEKKMNSELSLSHKKEEDLLRENSMLQEEIAMLISGDWN
```
### [2]. How to Run Package:

#### [2.1] Install Dependencies
```console
user@machine:~$ pip install -r requirements.txt
```
#### [2.2] Test Command-line #1: Run on AntiCancer Main Dataset
```console
user@machine:~$ python main.py
```

#### [2.3] Test Command-line #2: Run on different dataset
```console
user@machine:~$ python main.py -fa train_data.fasta -la train_data_label.txt -fa_i test_data.fasta -la_i tes_data_label.txt
```

**Table 1:**  command line element
| Symbol  | Explanation  |
| ------- | ------------ |
| -fa | Fasta file with .txt or .fasta format  |
| -la | Label file with .txt extension | 
| -fa_i | Independent set fasta file with .txt or .fasta format  |
| -la_i | Independent set label file with .txt extension  
