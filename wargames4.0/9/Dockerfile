FROM ubuntu:latest

LABEL org.opencontainers.image.source=https://github.com/Walchand-Linux-Users-Group/linux-diary

RUN apt-get update

RUN mkdir /home/wlug

WORKDIR /home/wlug

RUN echo "DoYouKnowMe">.itmaybehere00

RUN echo "HexMe">.itmaybehere01

RUN echo "OctMe">.itmaybehere02

RUN echo "BinMe">.itmaybehere03

RUN chmod 444 .itmaybehere00

RUN chmod 444 .itmaybehere01

RUN chmod 444 .itmaybehere02

RUN chmod 444 .itmaybehere03

RUN echo "mndnnwejnjesrehtomorf plehemostegnacew ebyamsneppahtahw txetsirewejyrtstel">answer00

RUN echo "amdsmzmmdjiejmekn sniondplehnacesle emosebyamtxet sirewejemosmaineveyeh">answer01

RUN echo "flahdnocesebnac erehwflahtsujstitub niagaemaseblliwtigniknihtyllaeruoyera siyekfotraptsrifehtyllanifemtoguoy">answer02

RUN echo "rewsnarofmeht kcehcplehnacyeht ebyamsrehtoksa txetsirewejemosmai">answer03

RUN chmod 444 answer00

RUN chmod 444 answer01

RUN chmod 444 answer02

RUN chmod 444 answer03

RUN gzip answer00

RUN gzip answer01

RUN gzip answer02

RUN gzip answer03

WORKDIR /home

RUN echo "1) New Day, New Tasks !!! \n2) Since, you have solved first day easily. No Hints this Time !!!\n\n\n3) Possible Commands for the task -> cd, ls, od, gunzip, zcat, rev\n\nAll The Best !!!">README

RUN chmod 444 README

CMD ["/bin/bash"]