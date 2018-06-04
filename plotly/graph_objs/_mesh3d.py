from plotly.basedatatypes import BaseTraceType


class Mesh3d(BaseTraceType):

    # alphahull
    # ---------
    @property
    def alphahull(self):
        """
        Determines how the mesh surface triangles are derived from the
        set of vertices (points) represented by the `x`, `y` and `z`
        arrays, if the `i`, `j`, `k` arrays are not supplied. For
        general use of `mesh3d` it is preferred that `i`, `j`, `k` are
        supplied. If *-1*, Delaunay triangulation is used, which is
        mainly suitable if the mesh is a single, more or less layer
        surface that is perpendicular to `delaunayaxis`. In case the
        `delaunayaxis` intersects the mesh surface at more than one
        point it will result triangles that are very long in the
        dimension of `delaunayaxis`. If *>0*, the alpha-shape algorithm
        is used. In this case, the positive `alphahull` value signals
        the use of the alpha-shape algorithm, _and_ its value acts as
        the parameter for the mesh fitting. If *0*,  the convex-hull
        algorithm is used. It is suitable for convex bodies or if the
        intention is to enclose the `x`, `y` and `z` point set into a
        convex hull.
    
        The 'alphahull' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['alphahull']

    @alphahull.setter
    def alphahull(self, val):
        self['alphahull'] = val

    # autocolorscale
    # --------------
    @property
    def autocolorscale(self):
        """
        Has an effect only if `color` is set to a numerical array.
        Determines whether the colorscale is a default palette
        (`autocolorscale: true`) or the palette determined by
        `colorscale`. In case `colorscale` is unspecified or
        `autocolorscale` is true, the default  palette will be chosen
        according to whether numbers in the `color` array are all
        positive, all negative or mixed.
    
        The 'autocolorscale' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['autocolorscale']

    @autocolorscale.setter
    def autocolorscale(self, val):
        self['autocolorscale'] = val

    # cauto
    # -----
    @property
    def cauto(self):
        """
        Has an effect only if `color` is set to a numerical array and
        `cmin`, `cmax` are set by the user. In this case, it controls
        whether the range of colors in `colorscale` is mapped to the
        range of values in the `color` array (`cauto: true`), or the
        `cmin`/`cmax` values (`cauto: false`). Defaults to `false` when
        `cmin`, `cmax` are set by the user.
    
        The 'cauto' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['cauto']

    @cauto.setter
    def cauto(self, val):
        self['cauto'] = val

    # cmax
    # ----
    @property
    def cmax(self):
        """
        Has an effect only if `color` is set to a numerical array. Sets
        the upper bound of the color domain. Value should be associated
        to the `color` array index, and if set, `cmin` must be set as
        well.
    
        The 'cmax' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['cmax']

    @cmax.setter
    def cmax(self, val):
        self['cmax'] = val

    # cmin
    # ----
    @property
    def cmin(self):
        """
        Has an effect only if `color` is set to a numerical array. Sets
        the lower bound of the color domain. Value should be associated
        to the `color` array index, and if set, `cmax` must be set as
        well.
    
        The 'cmin' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['cmin']

    @cmin.setter
    def cmin(self, val):
        self['cmin'] = val

    # color
    # -----
    @property
    def color(self):
        """
        Sets the color of the whole mesh
    
        The 'color' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color:
                aliceblue, antiquewhite, aqua, aquamarine, azure,
                beige, bisque, black, blanchedalmond, blue,
                blueviolet, brown, burlywood, cadetblue,
                chartreuse, chocolate, coral, cornflowerblue,
                cornsilk, crimson, cyan, darkblue, darkcyan,
                darkgoldenrod, darkgray, darkgrey, darkgreen,
                darkkhaki, darkmagenta, darkolivegreen, darkorange,
                darkorchid, darkred, darksalmon, darkseagreen,
                darkslateblue, darkslategray, darkslategrey,
                darkturquoise, darkviolet, deeppink, deepskyblue,
                dimgray, dimgrey, dodgerblue, firebrick,
                floralwhite, forestgreen, fuchsia, gainsboro,
                ghostwhite, gold, goldenrod, gray, grey, green,
                greenyellow, honeydew, hotpink, indianred, indigo,
                ivory, khaki, lavender, lavenderblush, lawngreen,
                lemonchiffon, lightblue, lightcoral, lightcyan,
                lightgoldenrodyellow, lightgray, lightgrey,
                lightgreen, lightpink, lightsalmon, lightseagreen,
                lightskyblue, lightslategray, lightslategrey,
                lightsteelblue, lightyellow, lime, limegreen,
                linen, magenta, maroon, mediumaquamarine,
                mediumblue, mediumorchid, mediumpurple,
                mediumseagreen, mediumslateblue, mediumspringgreen,
                mediumturquoise, mediumvioletred, midnightblue,
                mintcream, mistyrose, moccasin, navajowhite, navy,
                oldlace, olive, olivedrab, orange, orangered,
                orchid, palegoldenrod, palegreen, paleturquoise,
                palevioletred, papayawhip, peachpuff, peru, pink,
                plum, powderblue, purple, red, rosybrown,
                royalblue, saddlebrown, salmon, sandybrown,
                seagreen, seashell, sienna, silver, skyblue,
                slateblue, slategray, slategrey, snow, springgreen,
                steelblue, tan, teal, thistle, tomato, turquoise,
                violet, wheat, white, whitesmoke, yellow,
                yellowgreen
          - A number that will be interpreted as a color
            according to mesh3d.colorscale

        Returns
        -------
        str
        """
        return self['color']

    @color.setter
    def color(self, val):
        self['color'] = val

    # colorbar
    # --------
    @property
    def colorbar(self):
        """
        The 'colorbar' property is an instance of ColorBar
        that may be specified as:
          - An instance of plotly.graph_objs.mesh3d.ColorBar
          - A dict of string/value properties that will be passed
            to the ColorBar constructor
    
            Supported dict properties:
                
                bgcolor
                    Sets the color of padded area.
                bordercolor
                    Sets the axis line color.
                borderwidth
                    Sets the width (in px) or the border enclosing
                    this color bar.
                dtick
                    Sets the step in-between ticks on this axis.
                    Use with `tick0`. Must be a positive number, or
                    special strings available to *log* and *date*
                    axes. If the axis `type` is *log*, then ticks
                    are set every 10^(n*dtick) where n is the tick
                    number. For example, to set a tick mark at 1,
                    10, 100, 1000, ... set dtick to 1. To set tick
                    marks at 1, 100, 10000, ... set dtick to 2. To
                    set tick marks at 1, 5, 25, 125, 625, 3125, ...
                    set dtick to log_10(5), or 0.69897000433. *log*
                    has several special values; *L<f>*, where `f`
                    is a positive number, gives ticks linearly
                    spaced in value (but not position). For example
                    `tick0` = 0.1, `dtick` = *L0.5* will put ticks
                    at 0.1, 0.6, 1.1, 1.6 etc. To show powers of 10
                    plus small digits between, use *D1* (all
                    digits) or *D2* (only 2 and 5). `tick0` is
                    ignored for *D1* and *D2*. If the axis `type`
                    is *date*, then you must convert the time to
                    milliseconds. For example, to set the interval
                    between ticks to one day, set `dtick` to
                    86400000.0. *date* also has special values
                    *M<n>* gives ticks spaced by a number of
                    months. `n` must be a positive integer. To set
                    ticks on the 15th of every third month, set
                    `tick0` to *2000-01-15* and `dtick` to *M3*. To
                    set ticks every 4 years, set `dtick` to *M48*
                exponentformat
                    Determines a formatting rule for the tick
                    exponents. For example, consider the number
                    1,000,000,000. If *none*, it appears as
                    1,000,000,000. If *e*, 1e+9. If *E*, 1E+9. If
                    *power*, 1x10^9 (with 9 in a super script). If
                    *SI*, 1G. If *B*, 1B.
                len
                    Sets the length of the color bar This measure
                    excludes the padding of both ends. That is, the
                    color bar length is this length minus the
                    padding on both ends.
                lenmode
                    Determines whether this color bar's length
                    (i.e. the measure in the color variation
                    direction) is set in units of plot *fraction*
                    or in *pixels. Use `len` to set the value.
                nticks
                    Specifies the maximum number of ticks for the
                    particular axis. The actual number of ticks
                    will be chosen automatically to be less than or
                    equal to `nticks`. Has an effect only if
                    `tickmode` is set to *auto*.
                outlinecolor
                    Sets the axis line color.
                outlinewidth
                    Sets the width (in px) of the axis line.
                separatethousands
                    If "true", even 4-digit integers are separated
                showexponent
                    If *all*, all exponents are shown besides their
                    significands. If *first*, only the exponent of
                    the first tick is shown. If *last*, only the
                    exponent of the last tick is shown. If *none*,
                    no exponents appear.
                showticklabels
                    Determines whether or not the tick labels are
                    drawn.
                showtickprefix
                    If *all*, all tick labels are displayed with a
                    prefix. If *first*, only the first tick is
                    displayed with a prefix. If *last*, only the
                    last tick is displayed with a suffix. If
                    *none*, tick prefixes are hidden.
                showticksuffix
                    Same as `showtickprefix` but for tick suffixes.
                thickness
                    Sets the thickness of the color bar This
                    measure excludes the size of the padding, ticks
                    and labels.
                thicknessmode
                    Determines whether this color bar's thickness
                    (i.e. the measure in the constant color
                    direction) is set in units of plot *fraction*
                    or in *pixels*. Use `thickness` to set the
                    value.
                tick0
                    Sets the placement of the first tick on this
                    axis. Use with `dtick`. If the axis `type` is
                    *log*, then you must take the log of your
                    starting tick (e.g. to set the starting tick to
                    100, set the `tick0` to 2) except when
                    `dtick`=*L<f>* (see `dtick` for more info). If
                    the axis `type` is *date*, it should be a date
                    string, like date data. If the axis `type` is
                    *category*, it should be a number, using the
                    scale where each category is assigned a serial
                    number from zero in the order it appears.
                tickangle
                    Sets the angle of the tick labels with respect
                    to the horizontal. For example, a `tickangle`
                    of -90 draws the tick labels vertically.
                tickcolor
                    Sets the tick color.
                tickfont
                    Sets the color bar's tick label font
                tickformat
                    Sets the tick label formatting rule using d3
                    formatting mini-languages which are very
                    similar to those in Python. For numbers, see: h
                    ttps://github.com/d3/d3-format/blob/master/READ
                    ME.md#locale_format And for dates see:
                    https://github.com/d3/d3-time-
                    format/blob/master/README.md#locale_format We
                    add one item to d3's date formatter: *%{n}f*
                    for fractional seconds with n digits. For
                    example, *2016-10-13 09:15:23.456* with
                    tickformat *%H~%M~%S.%2f* would display
                    *09~15~23.46*
                tickformatstops
                    plotly.graph_objs.mesh3d.colorbar.Tickformatsto
                    p instance or dict with compatible properties
                ticklen
                    Sets the tick length (in px).
                tickmode
                    Sets the tick mode for this axis. If *auto*,
                    the number of ticks is set via `nticks`. If
                    *linear*, the placement of the ticks is
                    determined by a starting position `tick0` and a
                    tick step `dtick` (*linear* is the default
                    value if `tick0` and `dtick` are provided). If
                    *array*, the placement of the ticks is set via
                    `tickvals` and the tick text is `ticktext`.
                    (*array* is the default value if `tickvals` is
                    provided).
                tickprefix
                    Sets a tick label prefix.
                ticks
                    Determines whether ticks are drawn or not. If
                    **, this axis' ticks are not drawn. If
                    *outside* (*inside*), this axis' are drawn
                    outside (inside) the axis lines.
                ticksuffix
                    Sets a tick label suffix.
                ticktext
                    Sets the text displayed at the ticks position
                    via `tickvals`. Only has an effect if
                    `tickmode` is set to *array*. Used with
                    `tickvals`.
                ticktextsrc
                    Sets the source reference on plot.ly for
                    ticktext .
                tickvals
                    Sets the values at which ticks on this axis
                    appear. Only has an effect if `tickmode` is set
                    to *array*. Used with `ticktext`.
                tickvalssrc
                    Sets the source reference on plot.ly for
                    tickvals .
                tickwidth
                    Sets the tick width (in px).
                title
                    Sets the title of the color bar.
                titlefont
                    Sets this color bar's title font.
                titleside
                    Determines the location of the colorbar title
                    with respect to the color bar.
                x
                    Sets the x position of the color bar (in plot
                    fraction).
                xanchor
                    Sets this color bar's horizontal position
                    anchor. This anchor binds the `x` position to
                    the *left*, *center* or *right* of the color
                    bar.
                xpad
                    Sets the amount of padding (in px) along the x
                    direction.
                y
                    Sets the y position of the color bar (in plot
                    fraction).
                yanchor
                    Sets this color bar's vertical position anchor
                    This anchor binds the `y` position to the
                    *top*, *middle* or *bottom* of the color bar.
                ypad
                    Sets the amount of padding (in px) along the y
                    direction.

        Returns
        -------
        plotly.graph_objs.mesh3d.ColorBar
        """
        return self['colorbar']

    @colorbar.setter
    def colorbar(self, val):
        self['colorbar'] = val

    # colorscale
    # ----------
    @property
    def colorscale(self):
        """
        Sets the colorscale and only has an effect if `color` is set to
        a numerical array. The colorscale must be an array containing
        arrays mapping a normalized value to an rgb, rgba, hex, hsl,
        hsv, or named color string. At minimum, a mapping for the
        lowest (0) and highest (1) values are required. For example,
        `[[0, 'rgb(0,0,255)', [1, 'rgb(255,0,0)']]`. To control the
        bounds of the colorscale in color space, use `cmin` and `cmax`.
        Alternatively, `colorscale` may be a palette name string of the
        following list: Greys, YlGnBu, Greens, YlOrRd, Bluered, RdBu,
        Reds, Blues, Picnic, Rainbow, Portland, Jet, Hot, Blackbody,
        Earth, Electric, Viridis, Cividis
    
        The 'colorscale' property is a colorscale and may be
        specified as:
          - A list of 2-element lists where the first element is the
            normalized color level value (starting at 0 and ending at 1), 
            and the second item is a valid color string.
            (e.g. [[0, 'green'], [0.5, 'red'], [1.0, 'rgb(0, 0, 255)']])
          - One of the following named colorscales:
                ['Greys', 'YlGnBu', 'Greens', 'YlOrRd', 'Bluered', 'RdBu',
                'Reds', 'Blues', 'Picnic', 'Rainbow', 'Portland', 'Jet',
                'Hot', 'Blackbody', 'Earth', 'Electric', 'Viridis']

        Returns
        -------
        str
        """
        return self['colorscale']

    @colorscale.setter
    def colorscale(self, val):
        self['colorscale'] = val

    # contour
    # -------
    @property
    def contour(self):
        """
        The 'contour' property is an instance of Contour
        that may be specified as:
          - An instance of plotly.graph_objs.mesh3d.Contour
          - A dict of string/value properties that will be passed
            to the Contour constructor
    
            Supported dict properties:
                
                color
                    Sets the color of the contour lines.
                show
                    Sets whether or not dynamic contours are shown
                    on hover
                width
                    Sets the width of the contour lines.

        Returns
        -------
        plotly.graph_objs.mesh3d.Contour
        """
        return self['contour']

    @contour.setter
    def contour(self, val):
        self['contour'] = val

    # customdata
    # ----------
    @property
    def customdata(self):
        """
        Assigns extra data each datum. This may be useful when
        listening to hover, click and selection events. Note that,
        *scatter* traces also appends customdata items in the markers
        DOM elements
    
        The 'customdata' property is an array that may be specified as a tuple,
        list, one-dimensional numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['customdata']

    @customdata.setter
    def customdata(self, val):
        self['customdata'] = val

    # customdatasrc
    # -------------
    @property
    def customdatasrc(self):
        """
        Sets the source reference on plot.ly for  customdata .
    
        The 'customdatasrc' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['customdatasrc']

    @customdatasrc.setter
    def customdatasrc(self, val):
        self['customdatasrc'] = val

    # delaunayaxis
    # ------------
    @property
    def delaunayaxis(self):
        """
        Sets the Delaunay axis, which is the axis that is perpendicular
        to the surface of the Delaunay triangulation. It has an effect
        if `i`, `j`, `k` are not provided and `alphahull` is set to
        indicate Delaunay triangulation.
    
        The 'delaunayaxis' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['x', 'y', 'z']

        Returns
        -------
        Any
        """
        return self['delaunayaxis']

    @delaunayaxis.setter
    def delaunayaxis(self, val):
        self['delaunayaxis'] = val

    # facecolor
    # ---------
    @property
    def facecolor(self):
        """
        Sets the color of each face Overrides *color* and
        *vertexcolor*.
    
        The 'facecolor' property is an array that may be specified as a tuple,
        list, one-dimensional numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['facecolor']

    @facecolor.setter
    def facecolor(self, val):
        self['facecolor'] = val

    # facecolorsrc
    # ------------
    @property
    def facecolorsrc(self):
        """
        Sets the source reference on plot.ly for  facecolor .
    
        The 'facecolorsrc' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['facecolorsrc']

    @facecolorsrc.setter
    def facecolorsrc(self, val):
        self['facecolorsrc'] = val

    # flatshading
    # -----------
    @property
    def flatshading(self):
        """
        Determines whether or not normal smoothing is applied to the
        meshes, creating meshes with an angular, low-poly look via flat
        reflections.
    
        The 'flatshading' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['flatshading']

    @flatshading.setter
    def flatshading(self, val):
        self['flatshading'] = val

    # hoverinfo
    # ---------
    @property
    def hoverinfo(self):
        """
        Determines which trace information appear on hover. If `none`
        or `skip` are set, no information is displayed upon hovering.
        But, if `none` is set, click and hover events are still fired.
    
        The 'hoverinfo' property is a flaglist and may be specified
        as a string containing:
          - Any combination of ['x', 'y', 'z', 'text', 'name'] joined with '+' characters
            (e.g. 'x+y')
            OR exactly one of ['all', 'none', 'skip'] (e.g. 'skip')
          - A list or array of the above

        Returns
        -------
        Any|numpy.ndarray
        """
        return self['hoverinfo']

    @hoverinfo.setter
    def hoverinfo(self, val):
        self['hoverinfo'] = val

    # hoverinfosrc
    # ------------
    @property
    def hoverinfosrc(self):
        """
        Sets the source reference on plot.ly for  hoverinfo .
    
        The 'hoverinfosrc' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['hoverinfosrc']

    @hoverinfosrc.setter
    def hoverinfosrc(self, val):
        self['hoverinfosrc'] = val

    # hoverlabel
    # ----------
    @property
    def hoverlabel(self):
        """
        The 'hoverlabel' property is an instance of Hoverlabel
        that may be specified as:
          - An instance of plotly.graph_objs.mesh3d.Hoverlabel
          - A dict of string/value properties that will be passed
            to the Hoverlabel constructor
    
            Supported dict properties:
                
                bgcolor
                    Sets the background color of the hover labels
                    for this trace
                bgcolorsrc
                    Sets the source reference on plot.ly for
                    bgcolor .
                bordercolor
                    Sets the border color of the hover labels for
                    this trace.
                bordercolorsrc
                    Sets the source reference on plot.ly for
                    bordercolor .
                font
                    Sets the font used in hover labels.
                namelength
                    Sets the length (in number of characters) of
                    the trace name in the hover labels for this
                    trace. -1 shows the whole name regardless of
                    length. 0-3 shows the first 0-3 characters, and
                    an integer >3 will show the whole name if it is
                    less than that many characters, but if it is
                    longer, will truncate to `namelength - 3`
                    characters and add an ellipsis.
                namelengthsrc
                    Sets the source reference on plot.ly for
                    namelength .

        Returns
        -------
        plotly.graph_objs.mesh3d.Hoverlabel
        """
        return self['hoverlabel']

    @hoverlabel.setter
    def hoverlabel(self, val):
        self['hoverlabel'] = val

    # i
    # -
    @property
    def i(self):
        """
        A vector of vertex indices, i.e. integer values between 0 and
        the length of the vertex vectors, representing the *first*
        vertex of a triangle. For example, `{i[m], j[m], k[m]}`
        together represent face m (triangle m) in the mesh, where `i[m]
        = n` points to the triplet `{x[n], y[n], z[n]}` in the vertex
        arrays. Therefore, each element in `i` represents a point in
        space, which is the first vertex of a triangle.
    
        The 'i' property is an array that may be specified as a tuple,
        list, one-dimensional numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['i']

    @i.setter
    def i(self, val):
        self['i'] = val

    # ids
    # ---
    @property
    def ids(self):
        """
        Assigns id labels to each datum. These ids for object constancy
        of data points during animation. Should be an array of strings,
        not numbers or any other type.
    
        The 'ids' property is an array that may be specified as a tuple,
        list, one-dimensional numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['ids']

    @ids.setter
    def ids(self, val):
        self['ids'] = val

    # idssrc
    # ------
    @property
    def idssrc(self):
        """
        Sets the source reference on plot.ly for  ids .
    
        The 'idssrc' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['idssrc']

    @idssrc.setter
    def idssrc(self, val):
        self['idssrc'] = val

    # intensity
    # ---------
    @property
    def intensity(self):
        """
        Sets the vertex intensity values, used for plotting fields on
        meshes
    
        The 'intensity' property is an array that may be specified as a tuple,
        list, one-dimensional numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['intensity']

    @intensity.setter
    def intensity(self, val):
        self['intensity'] = val

    # intensitysrc
    # ------------
    @property
    def intensitysrc(self):
        """
        Sets the source reference on plot.ly for  intensity .
    
        The 'intensitysrc' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['intensitysrc']

    @intensitysrc.setter
    def intensitysrc(self, val):
        self['intensitysrc'] = val

    # isrc
    # ----
    @property
    def isrc(self):
        """
        Sets the source reference on plot.ly for  i .
    
        The 'isrc' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['isrc']

    @isrc.setter
    def isrc(self, val):
        self['isrc'] = val

    # j
    # -
    @property
    def j(self):
        """
        A vector of vertex indices, i.e. integer values between 0 and
        the length of the vertex vectors, representing the *second*
        vertex of a triangle. For example, `{i[m], j[m], k[m]}`
        together represent face m (triangle m) in the mesh, where `j[m]
        = n` points to the triplet `{x[n], y[n], z[n]}` in the vertex
        arrays. Therefore, each element in `j` represents a point in
        space, which is the second vertex of a triangle.
    
        The 'j' property is an array that may be specified as a tuple,
        list, one-dimensional numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['j']

    @j.setter
    def j(self, val):
        self['j'] = val

    # jsrc
    # ----
    @property
    def jsrc(self):
        """
        Sets the source reference on plot.ly for  j .
    
        The 'jsrc' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['jsrc']

    @jsrc.setter
    def jsrc(self, val):
        self['jsrc'] = val

    # k
    # -
    @property
    def k(self):
        """
        A vector of vertex indices, i.e. integer values between 0 and
        the length of the vertex vectors, representing the *third*
        vertex of a triangle. For example, `{i[m], j[m], k[m]}`
        together represent face m (triangle m) in the mesh, where `k[m]
        = n` points to the triplet  `{x[n], y[n], z[n]}` in the vertex
        arrays. Therefore, each element in `k` represents a point in
        space, which is the third vertex of a triangle.
    
        The 'k' property is an array that may be specified as a tuple,
        list, one-dimensional numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['k']

    @k.setter
    def k(self, val):
        self['k'] = val

    # ksrc
    # ----
    @property
    def ksrc(self):
        """
        Sets the source reference on plot.ly for  k .
    
        The 'ksrc' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['ksrc']

    @ksrc.setter
    def ksrc(self, val):
        self['ksrc'] = val

    # legendgroup
    # -----------
    @property
    def legendgroup(self):
        """
        Sets the legend group for this trace. Traces part of the same
        legend group hide/show at the same time when toggling legend
        items.
    
        The 'legendgroup' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['legendgroup']

    @legendgroup.setter
    def legendgroup(self, val):
        self['legendgroup'] = val

    # lighting
    # --------
    @property
    def lighting(self):
        """
        The 'lighting' property is an instance of Lighting
        that may be specified as:
          - An instance of plotly.graph_objs.mesh3d.Lighting
          - A dict of string/value properties that will be passed
            to the Lighting constructor
    
            Supported dict properties:
                
                ambient
                    Ambient light increases overall color
                    visibility but can wash out the image.
                diffuse
                    Represents the extent that incident rays are
                    reflected in a range of angles.
                facenormalsepsilon
                    Epsilon for face normals calculation avoids
                    math issues arising from degenerate geometry.
                fresnel
                    Represents the reflectance as a dependency of
                    the viewing angle; e.g. paper is reflective
                    when viewing it from the edge of the paper
                    (almost 90 degrees), causing shine.
                roughness
                    Alters specular reflection; the rougher the
                    surface, the wider and less contrasty the
                    shine.
                specular
                    Represents the level that incident rays are
                    reflected in a single direction, causing shine.
                vertexnormalsepsilon
                    Epsilon for vertex normals calculation avoids
                    math issues arising from degenerate geometry.

        Returns
        -------
        plotly.graph_objs.mesh3d.Lighting
        """
        return self['lighting']

    @lighting.setter
    def lighting(self, val):
        self['lighting'] = val

    # lightposition
    # -------------
    @property
    def lightposition(self):
        """
        The 'lightposition' property is an instance of Lightposition
        that may be specified as:
          - An instance of plotly.graph_objs.mesh3d.Lightposition
          - A dict of string/value properties that will be passed
            to the Lightposition constructor
    
            Supported dict properties:
                
                x
                    Numeric vector, representing the X coordinate
                    for each vertex.
                y
                    Numeric vector, representing the Y coordinate
                    for each vertex.
                z
                    Numeric vector, representing the Z coordinate
                    for each vertex.

        Returns
        -------
        plotly.graph_objs.mesh3d.Lightposition
        """
        return self['lightposition']

    @lightposition.setter
    def lightposition(self, val):
        self['lightposition'] = val

    # name
    # ----
    @property
    def name(self):
        """
        Sets the trace name. The trace name appear as the legend item
        and on hover.
    
        The 'name' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['name']

    @name.setter
    def name(self, val):
        self['name'] = val

    # opacity
    # -------
    @property
    def opacity(self):
        """
        Sets the opacity of the surface.
    
        The 'opacity' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self['opacity']

    @opacity.setter
    def opacity(self, val):
        self['opacity'] = val

    # reversescale
    # ------------
    @property
    def reversescale(self):
        """
        Has an effect only if `color` is set to a numerical array.
        Reverses the color mapping if true (`cmin` will correspond to
        the last color in the array and `cmax` will correspond to the
        first color).
    
        The 'reversescale' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['reversescale']

    @reversescale.setter
    def reversescale(self, val):
        self['reversescale'] = val

    # scene
    # -----
    @property
    def scene(self):
        """
        Sets a reference between this trace's 3D coordinate system and
        a 3D scene. If *scene* (the default value), the (x,y,z)
        coordinates refer to `layout.scene`. If *scene2*, the (x,y,z)
        coordinates refer to `layout.scene2`, and so on.
    
        The 'scene' property is an identifier of a particular
        subplot, of type 'scene', that may be specified as the string 'scene'
        optionally followed by an integer >= 1
        (e.g. 'scene', 'scene1', 'scene2', 'scene3', etc.)

        Returns
        -------
        str
        """
        return self['scene']

    @scene.setter
    def scene(self, val):
        self['scene'] = val

    # selectedpoints
    # --------------
    @property
    def selectedpoints(self):
        """
        Array containing integer indices of selected points. Has an
        effect only for traces that support selections. Note that an
        empty array means an empty selection where the `unselected` are
        turned on for all points, whereas, any other non-array values
        means no selection all where the `selected` and `unselected`
        styles have no effect.
    
        The 'selectedpoints' property accepts values of any type

        Returns
        -------
        Any
        """
        return self['selectedpoints']

    @selectedpoints.setter
    def selectedpoints(self, val):
        self['selectedpoints'] = val

    # showlegend
    # ----------
    @property
    def showlegend(self):
        """
        Determines whether or not an item corresponding to this trace
        is shown in the legend.
    
        The 'showlegend' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['showlegend']

    @showlegend.setter
    def showlegend(self, val):
        self['showlegend'] = val

    # showscale
    # ---------
    @property
    def showscale(self):
        """
        Determines whether or not a colorbar is displayed for this
        trace.
    
        The 'showscale' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['showscale']

    @showscale.setter
    def showscale(self, val):
        self['showscale'] = val

    # stream
    # ------
    @property
    def stream(self):
        """
        The 'stream' property is an instance of Stream
        that may be specified as:
          - An instance of plotly.graph_objs.mesh3d.Stream
          - A dict of string/value properties that will be passed
            to the Stream constructor
    
            Supported dict properties:
                
                maxpoints
                    Sets the maximum number of points to keep on
                    the plots from an incoming stream. If
                    `maxpoints` is set to *50*, only the newest 50
                    points will be displayed on the plot.
                token
                    The stream id number links a data trace on a
                    plot with a stream. See
                    https://plot.ly/settings for more details.

        Returns
        -------
        plotly.graph_objs.mesh3d.Stream
        """
        return self['stream']

    @stream.setter
    def stream(self, val):
        self['stream'] = val

    # text
    # ----
    @property
    def text(self):
        """
        Sets the text elements associated with the vertices. If trace
        `hoverinfo` contains a *text* flag and *hovertext* is not set,
        these elements will be seen in the hover labels.
    
        The 'text' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        str|numpy.ndarray
        """
        return self['text']

    @text.setter
    def text(self, val):
        self['text'] = val

    # textsrc
    # -------
    @property
    def textsrc(self):
        """
        Sets the source reference on plot.ly for  text .
    
        The 'textsrc' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['textsrc']

    @textsrc.setter
    def textsrc(self, val):
        self['textsrc'] = val

    # uid
    # ---
    @property
    def uid(self):
        """
        The 'uid' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['uid']

    @uid.setter
    def uid(self, val):
        self['uid'] = val

    # vertexcolor
    # -----------
    @property
    def vertexcolor(self):
        """
        Sets the color of each vertex Overrides *color*.
    
        The 'vertexcolor' property is an array that may be specified as a tuple,
        list, one-dimensional numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['vertexcolor']

    @vertexcolor.setter
    def vertexcolor(self, val):
        self['vertexcolor'] = val

    # vertexcolorsrc
    # --------------
    @property
    def vertexcolorsrc(self):
        """
        Sets the source reference on plot.ly for  vertexcolor .
    
        The 'vertexcolorsrc' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['vertexcolorsrc']

    @vertexcolorsrc.setter
    def vertexcolorsrc(self, val):
        self['vertexcolorsrc'] = val

    # visible
    # -------
    @property
    def visible(self):
        """
        Determines whether or not this trace is visible. If
        *legendonly*, the trace is not drawn, but can appear as a
        legend item (provided that the legend itself is visible).
    
        The 'visible' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                [True, False, 'legendonly']

        Returns
        -------
        Any
        """
        return self['visible']

    @visible.setter
    def visible(self, val):
        self['visible'] = val

    # x
    # -
    @property
    def x(self):
        """
        Sets the X coordinates of the vertices. The nth element of
        vectors `x`, `y` and `z` jointly represent the X, Y and Z
        coordinates of the nth vertex.
    
        The 'x' property is an array that may be specified as a tuple,
        list, one-dimensional numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['x']

    @x.setter
    def x(self, val):
        self['x'] = val

    # xcalendar
    # ---------
    @property
    def xcalendar(self):
        """
        Sets the calendar system to use with `x` date data.
    
        The 'xcalendar' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['gregorian', 'chinese', 'coptic', 'discworld',
                'ethiopian', 'hebrew', 'islamic', 'julian', 'mayan',
                'nanakshahi', 'nepali', 'persian', 'jalali', 'taiwan',
                'thai', 'ummalqura']

        Returns
        -------
        Any
        """
        return self['xcalendar']

    @xcalendar.setter
    def xcalendar(self, val):
        self['xcalendar'] = val

    # xsrc
    # ----
    @property
    def xsrc(self):
        """
        Sets the source reference on plot.ly for  x .
    
        The 'xsrc' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['xsrc']

    @xsrc.setter
    def xsrc(self, val):
        self['xsrc'] = val

    # y
    # -
    @property
    def y(self):
        """
        Sets the Y coordinates of the vertices. The nth element of
        vectors `x`, `y` and `z` jointly represent the X, Y and Z
        coordinates of the nth vertex.
    
        The 'y' property is an array that may be specified as a tuple,
        list, one-dimensional numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['y']

    @y.setter
    def y(self, val):
        self['y'] = val

    # ycalendar
    # ---------
    @property
    def ycalendar(self):
        """
        Sets the calendar system to use with `y` date data.
    
        The 'ycalendar' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['gregorian', 'chinese', 'coptic', 'discworld',
                'ethiopian', 'hebrew', 'islamic', 'julian', 'mayan',
                'nanakshahi', 'nepali', 'persian', 'jalali', 'taiwan',
                'thai', 'ummalqura']

        Returns
        -------
        Any
        """
        return self['ycalendar']

    @ycalendar.setter
    def ycalendar(self, val):
        self['ycalendar'] = val

    # ysrc
    # ----
    @property
    def ysrc(self):
        """
        Sets the source reference on plot.ly for  y .
    
        The 'ysrc' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['ysrc']

    @ysrc.setter
    def ysrc(self, val):
        self['ysrc'] = val

    # z
    # -
    @property
    def z(self):
        """
        Sets the Z coordinates of the vertices. The nth element of
        vectors `x`, `y` and `z` jointly represent the X, Y and Z
        coordinates of the nth vertex.
    
        The 'z' property is an array that may be specified as a tuple,
        list, one-dimensional numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['z']

    @z.setter
    def z(self, val):
        self['z'] = val

    # zcalendar
    # ---------
    @property
    def zcalendar(self):
        """
        Sets the calendar system to use with `z` date data.
    
        The 'zcalendar' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['gregorian', 'chinese', 'coptic', 'discworld',
                'ethiopian', 'hebrew', 'islamic', 'julian', 'mayan',
                'nanakshahi', 'nepali', 'persian', 'jalali', 'taiwan',
                'thai', 'ummalqura']

        Returns
        -------
        Any
        """
        return self['zcalendar']

    @zcalendar.setter
    def zcalendar(self, val):
        self['zcalendar'] = val

    # zsrc
    # ----
    @property
    def zsrc(self):
        """
        Sets the source reference on plot.ly for  z .
    
        The 'zsrc' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['zsrc']

    @zsrc.setter
    def zsrc(self, val):
        self['zsrc'] = val

    # type
    # ----
    @property
    def type(self):
        return self._props['type']

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return ''

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        alphahull
            Determines how the mesh surface triangles are derived
            from the set of vertices (points) represented by the
            `x`, `y` and `z` arrays, if the `i`, `j`, `k` arrays
            are not supplied. For general use of `mesh3d` it is
            preferred that `i`, `j`, `k` are supplied. If *-1*,
            Delaunay triangulation is used, which is mainly
            suitable if the mesh is a single, more or less layer
            surface that is perpendicular to `delaunayaxis`. In
            case the `delaunayaxis` intersects the mesh surface at
            more than one point it will result triangles that are
            very long in the dimension of `delaunayaxis`. If *>0*,
            the alpha-shape algorithm is used. In this case, the
            positive `alphahull` value signals the use of the
            alpha-shape algorithm, _and_ its value acts as the
            parameter for the mesh fitting. If *0*,  the convex-
            hull algorithm is used. It is suitable for convex
            bodies or if the intention is to enclose the `x`, `y`
            and `z` point set into a convex hull.
        autocolorscale
            Has an effect only if `color` is set to a numerical
            array. Determines whether the colorscale is a default
            palette (`autocolorscale: true`) or the palette
            determined by `colorscale`. In case `colorscale` is
            unspecified or `autocolorscale` is true, the default
            palette will be chosen according to whether numbers in
            the `color` array are all positive, all negative or
            mixed.
        cauto
            Has an effect only if `color` is set to a numerical
            array and `cmin`, `cmax` are set by the user. In this
            case, it controls whether the range of colors in
            `colorscale` is mapped to the range of values in the
            `color` array (`cauto: true`), or the `cmin`/`cmax`
            values (`cauto: false`). Defaults to `false` when
            `cmin`, `cmax` are set by the user.
        cmax
            Has an effect only if `color` is set to a numerical
            array. Sets the upper bound of the color domain. Value
            should be associated to the `color` array index, and if
            set, `cmin` must be set as well.
        cmin
            Has an effect only if `color` is set to a numerical
            array. Sets the lower bound of the color domain. Value
            should be associated to the `color` array index, and if
            set, `cmax` must be set as well.
        color
            Sets the color of the whole mesh
        colorbar
            plotly.graph_objs.mesh3d.ColorBar instance or dict with
            compatible properties
        colorscale
            Sets the colorscale and only has an effect if `color`
            is set to a numerical array. The colorscale must be an
            array containing arrays mapping a normalized value to
            an rgb, rgba, hex, hsl, hsv, or named color string. At
            minimum, a mapping for the lowest (0) and highest (1)
            values are required. For example, `[[0, 'rgb(0,0,255)',
            [1, 'rgb(255,0,0)']]`. To control the bounds of the
            colorscale in color space, use `cmin` and `cmax`.
            Alternatively, `colorscale` may be a palette name
            string of the following list: Greys, YlGnBu, Greens,
            YlOrRd, Bluered, RdBu, Reds, Blues, Picnic, Rainbow,
            Portland, Jet, Hot, Blackbody, Earth, Electric,
            Viridis, Cividis
        contour
            plotly.graph_objs.mesh3d.Contour instance or dict with
            compatible properties
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, *scatter* traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        delaunayaxis
            Sets the Delaunay axis, which is the axis that is
            perpendicular to the surface of the Delaunay
            triangulation. It has an effect if `i`, `j`, `k` are
            not provided and `alphahull` is set to indicate
            Delaunay triangulation.
        facecolor
            Sets the color of each face Overrides *color* and
            *vertexcolor*.
        facecolorsrc
            Sets the source reference on plot.ly for  facecolor .
        flatshading
            Determines whether or not normal smoothing is applied
            to the meshes, creating meshes with an angular, low-
            poly look via flat reflections.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.mesh3d.Hoverlabel instance or dict
            with compatible properties
        i
            A vector of vertex indices, i.e. integer values between
            0 and the length of the vertex vectors, representing
            the *first* vertex of a triangle. For example, `{i[m],
            j[m], k[m]}` together represent face m (triangle m) in
            the mesh, where `i[m] = n` points to the triplet
            `{x[n], y[n], z[n]}` in the vertex arrays. Therefore,
            each element in `i` represents a point in space, which
            is the first vertex of a triangle.
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on plot.ly for  ids .
        intensity
            Sets the vertex intensity values, used for plotting
            fields on meshes
        intensitysrc
            Sets the source reference on plot.ly for  intensity .
        isrc
            Sets the source reference on plot.ly for  i .
        j
            A vector of vertex indices, i.e. integer values between
            0 and the length of the vertex vectors, representing
            the *second* vertex of a triangle. For example, `{i[m],
            j[m], k[m]}`  together represent face m (triangle m) in
            the mesh, where `j[m] = n` points to the triplet
            `{x[n], y[n], z[n]}` in the vertex arrays. Therefore,
            each element in `j` represents a point in space, which
            is the second vertex of a triangle.
        jsrc
            Sets the source reference on plot.ly for  j .
        k
            A vector of vertex indices, i.e. integer values between
            0 and the length of the vertex vectors, representing
            the *third* vertex of a triangle. For example, `{i[m],
            j[m], k[m]}` together represent face m (triangle m) in
            the mesh, where `k[m] = n` points to the triplet
            `{x[n], y[n], z[n]}` in the vertex arrays. Therefore,
            each element in `k` represents a point in space, which
            is the third vertex of a triangle.
        ksrc
            Sets the source reference on plot.ly for  k .
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        lighting
            plotly.graph_objs.mesh3d.Lighting instance or dict with
            compatible properties
        lightposition
            plotly.graph_objs.mesh3d.Lightposition instance or dict
            with compatible properties
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the surface.
        reversescale
            Has an effect only if `color` is set to a numerical
            array. Reverses the color mapping if true (`cmin` will
            correspond to the last color in the array and `cmax`
            will correspond to the first color).
        scene
            Sets a reference between this trace's 3D coordinate
            system and a 3D scene. If *scene* (the default value),
            the (x,y,z) coordinates refer to `layout.scene`. If
            *scene2*, the (x,y,z) coordinates refer to
            `layout.scene2`, and so on.
        selectedpoints
            Array containing integer indices of selected points.
            Has an effect only for traces that support selections.
            Note that an empty array means an empty selection where
            the `unselected` are turned on for all points, whereas,
            any other non-array values means no selection all where
            the `selected` and `unselected` styles have no effect.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        showscale
            Determines whether or not a colorbar is displayed for
            this trace.
        stream
            plotly.graph_objs.mesh3d.Stream instance or dict with
            compatible properties
        text
            Sets the text elements associated with the vertices. If
            trace `hoverinfo` contains a *text* flag and
            *hovertext* is not set, these elements will be seen in
            the hover labels.
        textsrc
            Sets the source reference on plot.ly for  text .
        uid

        vertexcolor
            Sets the color of each vertex Overrides *color*.
        vertexcolorsrc
            Sets the source reference on plot.ly for  vertexcolor .
        visible
            Determines whether or not this trace is visible. If
            *legendonly*, the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        x
            Sets the X coordinates of the vertices. The nth element
            of vectors `x`, `y` and `z` jointly represent the X, Y
            and Z coordinates of the nth vertex.
        xcalendar
            Sets the calendar system to use with `x` date data.
        xsrc
            Sets the source reference on plot.ly for  x .
        y
            Sets the Y coordinates of the vertices. The nth element
            of vectors `x`, `y` and `z` jointly represent the X, Y
            and Z coordinates of the nth vertex.
        ycalendar
            Sets the calendar system to use with `y` date data.
        ysrc
            Sets the source reference on plot.ly for  y .
        z
            Sets the Z coordinates of the vertices. The nth element
            of vectors `x`, `y` and `z` jointly represent the X, Y
            and Z coordinates of the nth vertex.
        zcalendar
            Sets the calendar system to use with `z` date data.
        zsrc
            Sets the source reference on plot.ly for  z .
        """

    def __init__(
        self,
        alphahull=None,
        autocolorscale=None,
        cauto=None,
        cmax=None,
        cmin=None,
        color=None,
        colorbar=None,
        colorscale=None,
        contour=None,
        customdata=None,
        customdatasrc=None,
        delaunayaxis=None,
        facecolor=None,
        facecolorsrc=None,
        flatshading=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        i=None,
        ids=None,
        idssrc=None,
        intensity=None,
        intensitysrc=None,
        isrc=None,
        j=None,
        jsrc=None,
        k=None,
        ksrc=None,
        legendgroup=None,
        lighting=None,
        lightposition=None,
        name=None,
        opacity=None,
        reversescale=None,
        scene=None,
        selectedpoints=None,
        showlegend=None,
        showscale=None,
        stream=None,
        text=None,
        textsrc=None,
        uid=None,
        vertexcolor=None,
        vertexcolorsrc=None,
        visible=None,
        x=None,
        xcalendar=None,
        xsrc=None,
        y=None,
        ycalendar=None,
        ysrc=None,
        z=None,
        zcalendar=None,
        zsrc=None,
        **kwargs
    ):
        """
        Construct a new Mesh3d object
        
        Draws sets of triangles with coordinates given by three
        1-dimensional arrays in `x`, `y`, `z` and (1) a sets of `i`,
        `j`, `k` indices (2) Delaunay triangulation or (3) the Alpha-
        shape algorithm or (4) the Convex-hull algorithm

        Parameters
        ----------
        alphahull
            Determines how the mesh surface triangles are derived
            from the set of vertices (points) represented by the
            `x`, `y` and `z` arrays, if the `i`, `j`, `k` arrays
            are not supplied. For general use of `mesh3d` it is
            preferred that `i`, `j`, `k` are supplied. If *-1*,
            Delaunay triangulation is used, which is mainly
            suitable if the mesh is a single, more or less layer
            surface that is perpendicular to `delaunayaxis`. In
            case the `delaunayaxis` intersects the mesh surface at
            more than one point it will result triangles that are
            very long in the dimension of `delaunayaxis`. If *>0*,
            the alpha-shape algorithm is used. In this case, the
            positive `alphahull` value signals the use of the
            alpha-shape algorithm, _and_ its value acts as the
            parameter for the mesh fitting. If *0*,  the convex-
            hull algorithm is used. It is suitable for convex
            bodies or if the intention is to enclose the `x`, `y`
            and `z` point set into a convex hull.
        autocolorscale
            Has an effect only if `color` is set to a numerical
            array. Determines whether the colorscale is a default
            palette (`autocolorscale: true`) or the palette
            determined by `colorscale`. In case `colorscale` is
            unspecified or `autocolorscale` is true, the default
            palette will be chosen according to whether numbers in
            the `color` array are all positive, all negative or
            mixed.
        cauto
            Has an effect only if `color` is set to a numerical
            array and `cmin`, `cmax` are set by the user. In this
            case, it controls whether the range of colors in
            `colorscale` is mapped to the range of values in the
            `color` array (`cauto: true`), or the `cmin`/`cmax`
            values (`cauto: false`). Defaults to `false` when
            `cmin`, `cmax` are set by the user.
        cmax
            Has an effect only if `color` is set to a numerical
            array. Sets the upper bound of the color domain. Value
            should be associated to the `color` array index, and if
            set, `cmin` must be set as well.
        cmin
            Has an effect only if `color` is set to a numerical
            array. Sets the lower bound of the color domain. Value
            should be associated to the `color` array index, and if
            set, `cmax` must be set as well.
        color
            Sets the color of the whole mesh
        colorbar
            plotly.graph_objs.mesh3d.ColorBar instance or dict with
            compatible properties
        colorscale
            Sets the colorscale and only has an effect if `color`
            is set to a numerical array. The colorscale must be an
            array containing arrays mapping a normalized value to
            an rgb, rgba, hex, hsl, hsv, or named color string. At
            minimum, a mapping for the lowest (0) and highest (1)
            values are required. For example, `[[0, 'rgb(0,0,255)',
            [1, 'rgb(255,0,0)']]`. To control the bounds of the
            colorscale in color space, use `cmin` and `cmax`.
            Alternatively, `colorscale` may be a palette name
            string of the following list: Greys, YlGnBu, Greens,
            YlOrRd, Bluered, RdBu, Reds, Blues, Picnic, Rainbow,
            Portland, Jet, Hot, Blackbody, Earth, Electric,
            Viridis, Cividis
        contour
            plotly.graph_objs.mesh3d.Contour instance or dict with
            compatible properties
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, *scatter* traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        delaunayaxis
            Sets the Delaunay axis, which is the axis that is
            perpendicular to the surface of the Delaunay
            triangulation. It has an effect if `i`, `j`, `k` are
            not provided and `alphahull` is set to indicate
            Delaunay triangulation.
        facecolor
            Sets the color of each face Overrides *color* and
            *vertexcolor*.
        facecolorsrc
            Sets the source reference on plot.ly for  facecolor .
        flatshading
            Determines whether or not normal smoothing is applied
            to the meshes, creating meshes with an angular, low-
            poly look via flat reflections.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.mesh3d.Hoverlabel instance or dict
            with compatible properties
        i
            A vector of vertex indices, i.e. integer values between
            0 and the length of the vertex vectors, representing
            the *first* vertex of a triangle. For example, `{i[m],
            j[m], k[m]}` together represent face m (triangle m) in
            the mesh, where `i[m] = n` points to the triplet
            `{x[n], y[n], z[n]}` in the vertex arrays. Therefore,
            each element in `i` represents a point in space, which
            is the first vertex of a triangle.
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on plot.ly for  ids .
        intensity
            Sets the vertex intensity values, used for plotting
            fields on meshes
        intensitysrc
            Sets the source reference on plot.ly for  intensity .
        isrc
            Sets the source reference on plot.ly for  i .
        j
            A vector of vertex indices, i.e. integer values between
            0 and the length of the vertex vectors, representing
            the *second* vertex of a triangle. For example, `{i[m],
            j[m], k[m]}`  together represent face m (triangle m) in
            the mesh, where `j[m] = n` points to the triplet
            `{x[n], y[n], z[n]}` in the vertex arrays. Therefore,
            each element in `j` represents a point in space, which
            is the second vertex of a triangle.
        jsrc
            Sets the source reference on plot.ly for  j .
        k
            A vector of vertex indices, i.e. integer values between
            0 and the length of the vertex vectors, representing
            the *third* vertex of a triangle. For example, `{i[m],
            j[m], k[m]}` together represent face m (triangle m) in
            the mesh, where `k[m] = n` points to the triplet
            `{x[n], y[n], z[n]}` in the vertex arrays. Therefore,
            each element in `k` represents a point in space, which
            is the third vertex of a triangle.
        ksrc
            Sets the source reference on plot.ly for  k .
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        lighting
            plotly.graph_objs.mesh3d.Lighting instance or dict with
            compatible properties
        lightposition
            plotly.graph_objs.mesh3d.Lightposition instance or dict
            with compatible properties
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the surface.
        reversescale
            Has an effect only if `color` is set to a numerical
            array. Reverses the color mapping if true (`cmin` will
            correspond to the last color in the array and `cmax`
            will correspond to the first color).
        scene
            Sets a reference between this trace's 3D coordinate
            system and a 3D scene. If *scene* (the default value),
            the (x,y,z) coordinates refer to `layout.scene`. If
            *scene2*, the (x,y,z) coordinates refer to
            `layout.scene2`, and so on.
        selectedpoints
            Array containing integer indices of selected points.
            Has an effect only for traces that support selections.
            Note that an empty array means an empty selection where
            the `unselected` are turned on for all points, whereas,
            any other non-array values means no selection all where
            the `selected` and `unselected` styles have no effect.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        showscale
            Determines whether or not a colorbar is displayed for
            this trace.
        stream
            plotly.graph_objs.mesh3d.Stream instance or dict with
            compatible properties
        text
            Sets the text elements associated with the vertices. If
            trace `hoverinfo` contains a *text* flag and
            *hovertext* is not set, these elements will be seen in
            the hover labels.
        textsrc
            Sets the source reference on plot.ly for  text .
        uid

        vertexcolor
            Sets the color of each vertex Overrides *color*.
        vertexcolorsrc
            Sets the source reference on plot.ly for  vertexcolor .
        visible
            Determines whether or not this trace is visible. If
            *legendonly*, the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        x
            Sets the X coordinates of the vertices. The nth element
            of vectors `x`, `y` and `z` jointly represent the X, Y
            and Z coordinates of the nth vertex.
        xcalendar
            Sets the calendar system to use with `x` date data.
        xsrc
            Sets the source reference on plot.ly for  x .
        y
            Sets the Y coordinates of the vertices. The nth element
            of vectors `x`, `y` and `z` jointly represent the X, Y
            and Z coordinates of the nth vertex.
        ycalendar
            Sets the calendar system to use with `y` date data.
        ysrc
            Sets the source reference on plot.ly for  y .
        z
            Sets the Z coordinates of the vertices. The nth element
            of vectors `x`, `y` and `z` jointly represent the X, Y
            and Z coordinates of the nth vertex.
        zcalendar
            Sets the calendar system to use with `z` date data.
        zsrc
            Sets the source reference on plot.ly for  z .

        Returns
        -------
        Mesh3d
        """
        super(Mesh3d, self).__init__('mesh3d')

        # Import validators
        # -----------------
        from plotly.validators import (mesh3d as v_mesh3d)

        # Initialize validators
        # ---------------------
        self._validators['alphahull'] = v_mesh3d.AlphahullValidator()
        self._validators['autocolorscale'] = v_mesh3d.AutocolorscaleValidator()
        self._validators['cauto'] = v_mesh3d.CautoValidator()
        self._validators['cmax'] = v_mesh3d.CmaxValidator()
        self._validators['cmin'] = v_mesh3d.CminValidator()
        self._validators['color'] = v_mesh3d.ColorValidator()
        self._validators['colorbar'] = v_mesh3d.ColorBarValidator()
        self._validators['colorscale'] = v_mesh3d.ColorscaleValidator()
        self._validators['contour'] = v_mesh3d.ContourValidator()
        self._validators['customdata'] = v_mesh3d.CustomdataValidator()
        self._validators['customdatasrc'] = v_mesh3d.CustomdatasrcValidator()
        self._validators['delaunayaxis'] = v_mesh3d.DelaunayaxisValidator()
        self._validators['facecolor'] = v_mesh3d.FacecolorValidator()
        self._validators['facecolorsrc'] = v_mesh3d.FacecolorsrcValidator()
        self._validators['flatshading'] = v_mesh3d.FlatshadingValidator()
        self._validators['hoverinfo'] = v_mesh3d.HoverinfoValidator()
        self._validators['hoverinfosrc'] = v_mesh3d.HoverinfosrcValidator()
        self._validators['hoverlabel'] = v_mesh3d.HoverlabelValidator()
        self._validators['i'] = v_mesh3d.IValidator()
        self._validators['ids'] = v_mesh3d.IdsValidator()
        self._validators['idssrc'] = v_mesh3d.IdssrcValidator()
        self._validators['intensity'] = v_mesh3d.IntensityValidator()
        self._validators['intensitysrc'] = v_mesh3d.IntensitysrcValidator()
        self._validators['isrc'] = v_mesh3d.IsrcValidator()
        self._validators['j'] = v_mesh3d.JValidator()
        self._validators['jsrc'] = v_mesh3d.JsrcValidator()
        self._validators['k'] = v_mesh3d.KValidator()
        self._validators['ksrc'] = v_mesh3d.KsrcValidator()
        self._validators['legendgroup'] = v_mesh3d.LegendgroupValidator()
        self._validators['lighting'] = v_mesh3d.LightingValidator()
        self._validators['lightposition'] = v_mesh3d.LightpositionValidator()
        self._validators['name'] = v_mesh3d.NameValidator()
        self._validators['opacity'] = v_mesh3d.OpacityValidator()
        self._validators['reversescale'] = v_mesh3d.ReversescaleValidator()
        self._validators['scene'] = v_mesh3d.SceneValidator()
        self._validators['selectedpoints'] = v_mesh3d.SelectedpointsValidator()
        self._validators['showlegend'] = v_mesh3d.ShowlegendValidator()
        self._validators['showscale'] = v_mesh3d.ShowscaleValidator()
        self._validators['stream'] = v_mesh3d.StreamValidator()
        self._validators['text'] = v_mesh3d.TextValidator()
        self._validators['textsrc'] = v_mesh3d.TextsrcValidator()
        self._validators['uid'] = v_mesh3d.UidValidator()
        self._validators['vertexcolor'] = v_mesh3d.VertexcolorValidator()
        self._validators['vertexcolorsrc'] = v_mesh3d.VertexcolorsrcValidator()
        self._validators['visible'] = v_mesh3d.VisibleValidator()
        self._validators['x'] = v_mesh3d.XValidator()
        self._validators['xcalendar'] = v_mesh3d.XcalendarValidator()
        self._validators['xsrc'] = v_mesh3d.XsrcValidator()
        self._validators['y'] = v_mesh3d.YValidator()
        self._validators['ycalendar'] = v_mesh3d.YcalendarValidator()
        self._validators['ysrc'] = v_mesh3d.YsrcValidator()
        self._validators['z'] = v_mesh3d.ZValidator()
        self._validators['zcalendar'] = v_mesh3d.ZcalendarValidator()
        self._validators['zsrc'] = v_mesh3d.ZsrcValidator()

        # Populate data dict with properties
        # ----------------------------------
        self.alphahull = alphahull
        self.autocolorscale = autocolorscale
        self.cauto = cauto
        self.cmax = cmax
        self.cmin = cmin
        self.color = color
        self.colorbar = colorbar
        self.colorscale = colorscale
        self.contour = contour
        self.customdata = customdata
        self.customdatasrc = customdatasrc
        self.delaunayaxis = delaunayaxis
        self.facecolor = facecolor
        self.facecolorsrc = facecolorsrc
        self.flatshading = flatshading
        self.hoverinfo = hoverinfo
        self.hoverinfosrc = hoverinfosrc
        self.hoverlabel = hoverlabel
        self.i = i
        self.ids = ids
        self.idssrc = idssrc
        self.intensity = intensity
        self.intensitysrc = intensitysrc
        self.isrc = isrc
        self.j = j
        self.jsrc = jsrc
        self.k = k
        self.ksrc = ksrc
        self.legendgroup = legendgroup
        self.lighting = lighting
        self.lightposition = lightposition
        self.name = name
        self.opacity = opacity
        self.reversescale = reversescale
        self.scene = scene
        self.selectedpoints = selectedpoints
        self.showlegend = showlegend
        self.showscale = showscale
        self.stream = stream
        self.text = text
        self.textsrc = textsrc
        self.uid = uid
        self.vertexcolor = vertexcolor
        self.vertexcolorsrc = vertexcolorsrc
        self.visible = visible
        self.x = x
        self.xcalendar = xcalendar
        self.xsrc = xsrc
        self.y = y
        self.ycalendar = ycalendar
        self.ysrc = ysrc
        self.z = z
        self.zcalendar = zcalendar
        self.zsrc = zsrc

        # Read-only literals
        # ------------------
        from _plotly_utils.basevalidators import LiteralValidator
        self._props['type'] = 'mesh3d'
        self._validators['type'] = LiteralValidator(
            plotly_name='type', parent_name='mesh3d'
        )

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**kwargs)