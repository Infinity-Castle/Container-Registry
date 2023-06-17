FROM ubuntu:latest

LABEL org.opencontainers.image.source=https://github.com/Infinity-Castle/Wargames

RUN apt-get update

RUN mkdir /home/wlug

RUN mkdir /home/wlug/linuxDiary3.0

WORKDIR /home/wlug/linuxDiary3.0

RUN echo "iamsomejewerisfilewithsomejewerisdata maybeyoucantrysomeotherfile ormaybeicouldbetheanswerinsomeothercontainer">answer00

RUN echo "maybeyoucantrysomeotherfile ormaybeicouldbetheanswerinsomeothercontainer iamsomejewerisfilewithsomejewerisdata">answer01

RUN echo "maybeyoucantrysomeotherfile iamsomejewerisfilewithsomejewerisdata ormaybeicouldbetheanswerinsomeothercontainer">answer02

RUN echo "asdfasdfasdfYou Found Me !!! Flag : WLUG{4434455381}">answer03

RUN echo "againajewerisfile areyoueventrying makesuretocheckeverypossiblefile">answer04

RUN chmod 444 answer00

RUN chmod 444 answer01

RUN chmod 444 answer02

RUN chmod 444 answer03

RUN chmod 444 answer04

WORKDIR /home/wlug

RUN echo "\n\n\n1) You will start within the /home/wlug directory. \n2) Your Flag will be inside current directory only. \n3) Try To Look For a file with the Flag. \n4) Use the value of Flag to Unlock Next Level. \n\n\nPossible Commands for the task -> ls, cd, cat \n\n\nAll The Best !!! and lets start the game">README

RUN chmod 444 README

CMD ["/bin/bash"]
