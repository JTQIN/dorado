.. Quick Demo 2_:

Demo 2 - Using Lower-Level Functionality
----------------------------------------
In this demo, we show how particles can be placed on a gridded flow field generated using the `ANUGA <https://github.com/GeoscienceAustralia/anuga_core>`_ software package. Instead of specifying the number of iterations for the particles to walk, we will be specifying a target travel time for the particles to travel in this demo. To do this, we will use some of the lower-level functionality accessible in :download:`particle_track.py <../../../particlerouting/particle_track.py>`.

First we load the sample parameters and define our `Particle` object.

.. doctest::

   >>> import particlerouting as pr
   >>> anugaparams = pr.example_data.define_params.make_anuga_params()
   >>> particle = pr.particle_track.Particle(anugaparams)

We can visualize the flow discharge components for this scenario from the loaded parameters. The full script used to produce the below figures is available :download:`here <../pyplots/quickstart/demo2_flow.py>`.

.. doctest::

   >>> plt.subplot(1, 2, 1)
   >>> plt.imshow(anugaparams.qx)
   >>> plt.title('x-component of water discharge')
   >>> plt.subplot(1, 2, 2)
   >>> plt.imshow(anugaparams.qy)
   >>> plt.imshow(anugaparams.qy)
   >>> plt.title('y-component of water discharge')
   >>> plt.show()

.. plot:: quickstart/demo2_flow.py

Now let's route 50 particles with a target travel time of 2100 seconds. We will then visualize the final positions of the particles and display the final travel times associated with each of the particles to see how close they are to the target of 2100 seconds. Note that the `particlerouting` method of routing particles in discrete grid cells limits the precision which can be achieved in travel time values as the particles can only be located at the center of grid cells. The full script to produce the below figure and output is available :download:`here <../pyplots/quickstart/demo2.py>`.

.. doctest::

   >>> walk_data = particle.run_iteration(target_time=2100)
   >>> pr.routines.plot_initial(anugaparams.depth, walk_data)
   >>> pr.routines.plot_final(anugaparams.depth, walk_depth)
   >>> plt.title('Initial and Final Particle Locations')
   >>> plt.show()

.. plot:: quickstart/demo2.py

.. doctest::

   >>> finaltimes = []
   >>> for i in list(range(0, params.Np_tracer)):
   >>>    finaltimes.append(walk_data['travel_times'][i][-1])
   >>> print('List of particle travel times for final particle locations: ' +
   >>>       str(np.round(finaltimes)))

   List of particle travel times for final particle locations: [2158.
   2118. 2088. 2149. 2096. 2206. 2104. 2104. 2207. 2137. 2097. 2147.
   2032. 2118. 2084. 2037. 2066. 2076. 2104. 2108. 2033. 2101. 2080.
   2072. 2031. 2041. 2076. 2063. 2125. 2102. 2140. 2178. 2173. 2097.
   2104. 2189. 2061. 2112. 2074. 2095. 2100. 2177. 2069. 2032. 2050.
   2086. 2036. 2109. 2078. 2047.]