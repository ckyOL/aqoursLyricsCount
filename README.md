# Aqours Lyrics Count
### A Word Frequency Count of Aqours lyrics up to now(2017.11.5)

#### you can also use to count others idol group😀

## File

~~~bash
├── README.md            //the file you reading now
├── lyrics
│   ├── __init__.py
│   ├── lyric.py         //save all lyric
│   └── lyrics_get.py    //get lyric method
├── plot
│   ├── __init__.py
│   ├── plot.py          //plot bar(single)
│   └── total_plot.py    //plot bar(all data)
└── text
    ├── __init__.py
    ├── text.py          //count word frequency(single)
    ├── all_count.py     //count word frequency(all song)
    └── text_seg.py      //text segmentation method
~~~

## Usage

1. run lyric.py to fetch all lyric data.
2. run text.py(or all_count.py) to count word frequency which will be used to plot graph.
3. run plot.py(or total_plot.py) to plot graph.

## Have some trouble?

read this article of my blog [link](https://blog.ckyol.moe/2017/11/05/aqoursLyricsCount/)
