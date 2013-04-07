Android 4.2 developer options
#############################

:tags: Android, Linux, openSuse
:lang: hr
:slug: android-42-developer-options
:date: 2013-01-27

Nedavno sam ulovio vremena da na svoj Galaxy S mudrofon konačno stavim Android 4.2.1
i to kao `CM 10.1 M <http://www.cyanogenmod.org/blog/cm-10-1-m-series-builds-have-arrived>`_.
Stvar radi savšeno i za sad nisam naišao na probleme u
svakodnevnom korištenju. No, kad sam pokušao vidjeti kako se
`Linux za sve android app <https://github.com/linuxzasve/androidApp>`_
ponaša na novoj verziji Androida, nisam uspio uključiti debugging mod.
Naime, Android 4.2 nema u ``Settings`` izborniku stavke ``Developer options``,
gdje se uključuje ``Android debugging`` opcija koja omogućava debugiranje
android aplikacija direktno na uređaju koji je USB-om spojen na računalo, umjesto da
se koristi emulator.

Radi se o tome da je Google namjerno isključio tu stavku pod izlikom da ne treba nikome osim
developerima, a ovi pak znaju kako riješiti takve problemčiće.

Da bi se omogućila stavka ``Developer options`` potrebno je sedam puta kliknuti na
``Build number`` stavku u ``Settings -> About phone`` izborniku.

Čak se pojavi i zgodan `toast <http://developer.android.com/guide/topics/ui/notifiers/toasts.html>`_
popup koji odbrojava klikove, odnosono ispiše poruku ako
se klikne na ``Build number`` kad je već stavka uključena.

.. image:: /slike/android_42_enable_developer_options.png

Da bi se sada uređaj mogao koristiti za debugiranje
potrebno je napraviti sljedeće::

    Settings -> Developer Options -> Android debugging (staviti kvacicu)

Ako se sad pokuša pokrenuti app dobije se:

.. image:: http://dejanperetin.com/static/slike/android_prije_rulova.png


Detaljne upute za rješavanje ovog problema mogu se pronaći na
`Android developers <http://developer.android.com/tools/device.html>`_ stranici.

Ukratko, treba generirati fajl ::

    /etc/udev/rules.d/42-android-devices.rules

Sadržaja: ::

    SUBSYSTEM=="usb", ATTR{idVendor}=="04e8", MODE="0666", GROUP="users"

Uređaj još uvijek nije prepoznat jer je ``04e8`` Samsung oznaka. Budući da je na mobitel sada
instaliran CyanogenMod, radi se o Google uređaju, pa je za vendor vrijednost potrebno staviti ``18d1``.


Uređaj je sada uredno prepoznat (stari screenshot, zato piše verzija 2.3.3):

.. image:: http://dejanperetin.com/static/slike/android_nakon_rulova.png


