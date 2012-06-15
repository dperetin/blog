Raspberry Pi - prvi dojmovi
===========================

:tags: RPi, Raspberry Pi

Hardver
-------

Planirano je da Rapberry Pi dolazi u dvije varijanete, Model A i Model B. Model B je skuplja varijanta, zvanična cijena mu je 35 USD  no zasad se proizvodi samo taj model. 
Raspbery Pi model B pogoni Broadcom BCM2835 procesor koji kuca na 700 MHz. Model B također ima modul
od 256 Mb radne memorije koja se dijeli između centralnog procesora i grafičkog procesora. 
Po defaultu centralnom procesoru ostaje 186 MB. Prisutna su dva USB 2.0 priključka, HDMI izlaz, 
3.5mm audio i RCA kompozitni izlaz. 
Raspberry Pi se na mrežu može spojiti putem RJ45 ethernet porta koji dolazi isključivo u modelu B.

Ono što nećete dobiti uz Raspberry Pi, a nužno je za njegov rad je SD memorijska kartica.

SD kartica s predinstaliranim operativnim sustavom se može naručiti prilikom kupnje no u trenutnu naručivanja ovog uređaja bile su rasprodane. Dakle, za pokretanje Rasperry Pia potrebno je imati pri ruci jednu SD karticu kapaciteta barem 2 GB te se na nju mora nasnimiti slika koja sadrži operativni sustav. Na službenim download stranicama Raspberry Pia dostupne su tri takver slike, od
kojih se za početak preporučuje Debian squeeze pa smo se odlučili naše druženje s Piom započeti upravo tom slikom.


Instalacija slike
-----------------

Prvo je potrebno skinuti sliku koji planiramo staviti na SD karticu. U našem slučaju to 
debian6-19-04-2012.zip koji se nalazi na službenoj download stranici.

Zatim sliku treba otpakirati ::

    $ unzip debian6-19-04-2012.zip

Time se dobije debian6-19-04-2012.img datoteka koja sadrži sliku.

Da bi na SD karticu stavili sliku, potrebno je imati neki čitač kartica i spojiti karticu na računalo.
Zatim moramo utvrditi pod kojim imenom je kartica prepoznata:
Naredbom df -h možemo vidjeti novo mountane diskove te prepoznati našu SD karticu.
Ako izvršimo tu narednu prije i poslije umetanja kartice možemo uočiti nove zapise i prepoznati karticu

::

    $ df -h
    Filesystem      Size  Used Avail Use% Mounted on
    rootfs           19G  7.5G   10G  43% /
    devtmpfs        2.0G   36K  2.0G   1% /dev
    tmpfs           2.0G  2.6M  2.0G   1% /dev/shm
    tmpfs           2.0G  716K  2.0G   1% /run
    /dev/sda6        19G  7.5G   10G  43% /
    tmpfs           2.0G     0  2.0G   0% /sys/fs/cgroup
    tmpfs           2.0G  716K  2.0G   1% /var/lock
    tmpfs           2.0G  716K  2.0G   1% /var/run
    tmpfs           2.0G     0  2.0G   0% /media
    /dev/sda7       244G   30G  203G  13% /home
    /dev/sda2       196G  127G   69G  65% /windows/C
    /dev/sdd1        63M  6.0M   58M  10% /media/B757-8716
    /dev/sdd3       7.2G  1.6G  5.2G  24% /media/14fa9af4-552a-4f53-88ad-3259f189fccf

Vidimo da je kartica prepoznata kao /dev/sdd

Prije nastavka potrebno je unmountati sve particije koje se nalaze na kartici, u ovom slučaju to su /dev/sdd1 i /dev/sdd3

::

    umount /dev/sdd1
    umount /dev/sdd3

Slika se sada snimi na karticu sa kao root ::

    # dd bs=1M if=debian6-19-04-2012.img of=/dev/sdd

pa onda ::

    sync

Ovako priremljena kartica je dovoljna da se rasp pi boota.
Nema on off gumba. Stvar se usteka i radi. 
Prvi boot traje oko 4.5 monute. pi se boota u terminal i za to mu
obično treba oko jedne minute.

Defaultni user name za ovu sliku je pi i pripadni password je raspberry.

Prvo sto upada u oci je cinjenica da ovakav nacin pripremanja kartice koristi samo
onaj dio kartice koji je predviden slikom, odnosno 2 GB.

Iako je nasa testna kartica kapaciteta 8 GB, Pi vidi i koristi samo 2 GB.
Što korisniku ostavlja na koristenje cijelih 298 mb. Neke druge slike kao
recimo raspbmc se pobrinu da je cijla kartica raspoliživa.


::

    pi@raspberrypi:~$ df -h
    Filesystem            Size  Used Avail Use% Mounted on
    tmpfs                  94M     0   94M   0% /lib/init/rw
    udev                   10M  152K  9.9M   2% /dev
    tmpfs                  94M     0   94M   0% /dev/shm
    rootfs                1.6G  1.2G  298M  80% /
    /dev/mmcblk0p1         75M   28M   47M  37% /boot

Da bi doskočili ovom problemu potrebno je resajzati particiju:
(izvor https://www.youtube.com/watch?v=R4VovMDnsIE).

Disk na kojem je particija koju zelimo resajzati je /dev/mmcblk0, sufiks p1, p2 itd. su oznake particije.

Sve ovo radimo direktno na piu: ::

    sudo fdisk -uc /dev/mmcblk0

naredbom p izlistamo informacije o particijama.

::

    Command (m for help): p

    Disk /dev/mmcblk0: 7969 MB, 7969177600 bytes
    4 heads, 32 sectors/track, 121600 cylinders, total 15564800 sectors
    Units = sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disk identifier: 0x000ee283

            Device Boot      Start         End      Blocks   Id  System
    /dev/mmcblk0p1            2048      155647       76800    c  W95 FAT32 (LBA)
    /dev/mmcblk0p2          157696     3414015     1628160   83  Linux
    /dev/mmcblk0p3         3416064     3807231      195584   82  Linux swap / Solaris

Resajzamo particiju /dev/mmcblk0p2. 
Prvo izbrisemo particiju komandom d i damo mu broj particije 2

::

    Command (m for help): d
    Partition number (1-4): 2

    Command (m for help): d
    Partition number (1-4): 3

Sada napravimo particiju
n p 2 i za pocetak sektora treba staviti pocetak stare particije i za velicinu iyaveremo difaltnu vrijednost da yauyme cijelu karticu: ::

            Device Boot      Start         End      Blocks   Id  System
    /dev/mmcblk0p1            2048      155647       76800    c  W95 FAT32 (LBA)
    /dev/mmcblk0p2          157696     3414015     1628160   83  Linux
    /dev/mmcblk0p3         3416064     3807231      195584   82  Linux swap / Solaris

    Command (m for help): d
    Partition number (1-4): 2

    Command (m for help): d
    Partition number (1-4): 3

    Command (m for help): n
    Command action
       e   extended
       p   primary partition (1-4)
    p
    Partition number (1-4): p
    Partition number (1-4): 2
    First sector (155648-15564799, default 155648): 157696

w - commit changes

reboot

nakon ponovnog ulogiravanja napravimo resize ::

    sudo resize2fs /dev/mmcblk0p2

::

    pi@raspberrypi:~$ df -h
    Filesystem            Size  Used Avail Use% Mounted on
    tmpfs                  94M     0   94M   0% /lib/init/rw
    udev                   10M  148K  9.9M   2% /dev
    tmpfs                  94M     0   94M   0% /dev/shm
    rootfs                7.3G  1.2G  5.8G  17% /
    /dev/mmcblk0p1         75M   28M   47M  37% /boot

U jednom od prethodnih koraka odabrali smo opciju da se root particija prosiri na cijeli disk
pa sada nema mjesta za swap particiju. To cemo rijesiti ovako ::

    sudo dd if=/dev/zero of=/var/swapfile bs=1M count=128
    sudo mkswap /var/swapfile
    sudo swapon /var/swapfile
    reboot

Editirati datoteku:
/etc/fstab iz ovog: ::

    proc            /proc           proc    defaults        0       0
    /dev/mmcblk0p1  /boot           vfat    defaults        0       0
    #/dev/mmcblk0p3  none            swap    sw              0       0


u ovo: ::

    proc            /proc           proc    defaults                                0       0
    /dev/mmcblk0p1  /boot           vfat    defaults                                0       0
    /dev/mmcblk0p2  /               ext4    defaults,noatime,nodiratime             0       0
    /var/swapfile   none            swap    sw                                      0       0

Instalacija Raspbmc
-------------------

Sliku Raspbmc se moze skinuti s http://download.raspbmc.com/downloads/bin/ramdistribution/installer-testing.img.gz

Smjestanje slike na karticu se odvija isto kao u prethodnom koraku. 
Time se na karticu instalira installer. Dalje za instaliranje Raspbmc-a
potrebno je samo upaliti Raspberry Pi koji mora biti spojen na mrezu.
Installer ce sam obaviti sve poslove umjesto vas i instalirati os.

Za razliku od prethodnog slucaja.

Dojmovi
-------

Rpi se uredno spojio na mrezu (DHCP), tipkovnica i miš su također uredno prepoynati.
RPi je bio spojen na stari TV i slika i zvuk su uredno prenesena. 

USB konektori su smjesteni jako blizu jedan drugom, pa ako planirate imati spojen uređaj koji
je malo deblji, kao npr. USB stick ili wifi adapter, potrebno je imati nekak produzni ili hub.

koristi puni disk
