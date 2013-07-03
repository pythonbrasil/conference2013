Installation
------------

.. Note::
   ``conference2013`` has been tested in production with Plone 4.2.x only.

To enable this package in a buildout-based installation:

1. Edit your buildout.cfg and add add the following to it::

    [buildout]
    ...
    eggs =
        conference2013


After updating the configuration you need to run ''bin/buildout'', which will
take care of updating your system.

Go to the 'Site Setup' page in a Plone site and click on the 'Add-ons' link.

Check the box next to ``Plone Conference 2013`` and click the 'Activate' button.

Note: You may have to empty your browser cache and save your resource
registries in order to see the effects of the package installation.
