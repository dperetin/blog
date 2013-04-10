KDM i Grub stavke kod restarta
##############################

:tags: KDE, Linux, openSuse, KDM
:lang: hr
:slug: kdm-grub-listings
:date: 2013-04-08

Za ljude koji imaju više stavki na GRUB izborniku i često ih koriste.
U datoteci ``/usr/share/kde4/config/kdm/kdmrc`` postoji linija koja se 
odnosi na ``BootManager`` (zadnja u donjem kodu): ::

    $ cat /usr/share/kde4/config/kdm/kdmrc | grep -i "boot\s*manager"
    # The boot manager KDM should use for offering boot options in the
    # "None" - no boot manager
    # "Grub" - Grub boot manager
    # "Grub2" - Grub2 boot manager
    # "Burg" - Burg boot manager
    # "Lilo" - Lilo boot manager (Linux on i386 & x86-64 only)
    #BootManager=Grub

Ako se otkomentira i umjesto ``Grub`` stavi boot manager koji je instaliran 
(default kod opensuse-a 12.3 je ``Grub2``), kod restarta se dobije izbornik sa 
stavkama Gruba, sustav se boota u ono sto se izabere. Pri restartu izbor izgleda kao
dolje na slici.

.. image:: http://dejanperetin.com/static/slike/restart_grub_items.png


