import streamlit as st

st.title("!! DIP MENSURATION SOLVER !!")
st.image("mensuration.png")
skb = st.sidebar.radio("navigation", ["HOME", "MAIN_PAGE"])
if skb == "HOME":
    s, r = st.columns(2)
    if s.button("REFERENCE"):
        st.write("@ we have various source of formulas @")
        st.image("formula.jpg")
        if r.button("WORKING_MANUAL"):
            st.write(
                    "With the help of this package, you are going to get a lot of facilities in all the questions of mensuration..."
                    "It is even easier to use it.  First of all you will not have to be me, after that You will have as much of the data as you require."
                    " You will have to fill that data in it.  After that you will get the solution of your problem")
if skb == "MAIN_PAGE":
    sb = st.sidebar.selectbox("SELECT_ANY_ONE", ["RECTANGLE", "SQUARE", "CIRCLE", "CUBE", "CUBOID"])
    if sb == "RECTANGLE":
        l1 = st.selectbox("SELECT WHAT YOU WANT", ["AREA", "PERIMETER", "DIAGONAL"])
        if l1 == "AREA":
            p, q = st.columns(2)
            xy = p.number_input("enter the value of length", 1.0, 1000.0, step=1.0)
            yz = q.number_input("enter the value of bredth", 1.0, 1000.0, step=1.0)
            arr = xy * yz  # formula of area
            if st.button("check"):
                st.write("area =", arr)
                st.balloons()
                st.write("is it helpfull")
            if st.button("yes"):
                        st.write("thank you")
                        st.snow()
            elif st.button("no"):
                st.write("we'll improve") # this is for AREA

        elif l1 == "PERIMETER":
            rr, qq = st.columns(2)
            xx = rr.number_input("enter the value of length", 1.0, 1000.0, step=1.0)
            zz = qq.number_input("enter the value of bredth", 1.0, 1000.0, step=1.0)
            peri = 2*(xx + zz)# formula of perimeter
            if st.button("check"):
                st.write("PERIMETER =", peri)
                st.balloons()
                st.write("is it helpfull")
            if st.button("yes"):
                st.write("thank you")
                st.snow()
            elif st.button("no"):
                st.write("we'll improve") #this is for perimeter

        elif l1 == "DIAGONAL":
            r1, q1 = st.columns(2)
            x1 = r1.number_input("enter the value of length", 1.0, 1000.0, step=1.0)
            z1 = q1.number_input("enter the value of bredth", 1.0, 1000.0, step=1.0)
            x2= x1*x1 + z1*z1
            diao = x2*x2# formula of diagonal
            if st.button("check"):
                st.write("DIAGONAL =", diao)
                st.balloons()
                st.write("is it helpfull")
            if st.button("yes"):
                st.write("thank you")
                st.snow()
            elif st.button("no"):
                st.write("we'll improve")#this is for diagonal
                # from here we are starting thr squre thing
        elif sb == "SQUARE":
            l2 = st.selectbox("SELECT WHAT YOU WANT", ["AREA", "PERIMETER", "DIAGONAL"])
            if l2 == "AREA":
                xy1 = st.number_input("enter the value of length", 1.0, 1000.0, step=1.0)
                arr1 = xy1*xy1  # formula of area
            if st.button("check"):
                st.write("area =", arr1)
                st.balloons()
                st.write("is it helpfull")
            if st.button("yes"):
                st.write("thank you")
                st.snow()
            elif st.button("no"):
                st.write("we'll improve")  # this is for AREA

            elif l2 == "PERIMETER":
                xx1 = st.number_input("Enter the value of length", 1.0, 1000.0, step=1.0)
                peri1 = 4*xx1  # formula of perimeter
                if st.button("check"):
                    st.write("PERIMETER =", peri1)
                    st.balloons()
                    st.write("is it helpfull")
                if st.button("yes"):
                    st.write("thank you")
                    st.snow()
                elif st.button("no"):
                    st.write("we'll improve")  # this is for perimeter

            elif l2 == "DIAGONAL":
                x6 = st.number_input("enter the value of RADIUS", 1.0, 1000.0, step=1.0)
                diao1 = (2*x6*x6) *(2*x6*x6) # formula of diagonal
                if st.button("check"):
                    st.write("DIAGONAL =", diao1)
                    st.balloons()
                    st.write("is it helpfull")
                if st.button("yes"):
                    st.write("thank you")
                    st.snow()
                elif st.button("no"):
                            st.write("we'll improve")  # this is for diagonal
                            # from here we are starting thr circle thing

        elif sb == "CIRCLE":
            l3 = st.selectbox("SELECT WHAT YOU WANT", ["AREA", "CIRCUMFERENCE","RADIUS"])
            if l3 == "AREA":
                xxxx = st.number_input("enter the value of RASIUS", 1.0, 1000.0, step=1.0)
                arrr = 3.14 * xxxx*xxxx  # formula of area
                if st.button("check"):
                    st.write("area =", arrr)
                    st.balloons()
                    st.write("is it helpfull")
                if st.button("yes"):
                    st.write("thank you")
                    st.snow()
                elif st.button("no"):
                    st.write("we'll improve")  # this is for AREA

            elif l3 == "CIRCUMFERENCE":
                xx25 = st.number_input("Enter the value of length", 1.0, 1000.0, step=1.0)
                circu = 2 * 3.14 * xx25  # formula of perimeter
                if st.button("check"):
                    st.write("CIRCUMFERENCE =", circu)
                    st.balloons()
                    st.write("is it helpfull")
                if st.button("yes"):
                    st.write("thank you")
                    st.snow()
                elif st.button("no"):
                    st.write("we'll improve")  # this is for CIRCUMFERENCE

            elif l3 == "RADIUS":
                x252 = st.number_input("enter the value of AREA", 1.0, 1000.0, step=1.0)
                rad = (x252/3.14)  # formula of diagonal
                if st.button("check"):
                    st.write("RADIUS =", rad)
                    st.balloons()
                    st.write("is it helpfull")
                if st.button("yes"):
                    st.write("thank you")
                    st.snow()
                elif st.button("no"):
                    st.write("we'll improve")  # this is for RADIUS
                    # from here we are starting thr CUBE thing


        elif sb == "CUBE":
            l4 = st.selectbox("SELECT WHAT YOU WANT", ["VOLUME", "SURFACE_AREA","DIAGONAL"])
            if l4 == "VOLUME":
                x262 = st.number_input("enter the value of LENGTH", 1.0, 1000.0, step=1.0)
                vol = x262 * x262 * x262  # formula of volume
                if st.button("check"):
                    st.write("VOLUME =", vol)
                    st.balloons()
                    st.write("is it helpfull")
                if st.button("yes"):
                    st.write("thank you")
                    st.snow()
                elif st.button("no"):
                    st.write("we'll improve")  # this is for VOLUME

            elif l4 == "SURFACE_AREA":
                x34 = st.number_input("Enter the value of LENGTH", 1.0, 1000.0, step=1.0)
                sur_are = 6 * x34 * x34  # formula of SURFACE_AREA
                if st.button("check"):
                    st.write("SURFACE_AREA =", sur_are)
                    st.balloons()
                    st.write("is it helpfull")
                if st.button("yes"):
                    st.write("thank you")
                    st.snow()
                elif st.button("no"):
                    st.write("we'll improve")  # this is for SURFACE_AREA

            elif l4 == "DIAGONAL":
                x91 = st.number_input("enter the value of LENGTH", 1.0, 1000.0, step=1.0)
                diagona = 3 * x91 # formula of diagonal
                if st.button("check"):
                    st.write("DIAGONAL =", diagona)
                    st.balloons()
                    st.write("is it helpfull")
                if st.button("yes"):
                    st.write("thank you")
                    st.snow()
                elif st.button("no"):
                    st.write("we'll improve")  # this is for DIAGONAL
                    # from here we are starting thr CUBOID thing

        if sb == "CUBOID":
            l11 = st.selectbox("SELECT WHAT YOU WANT", ["VOLUME", "SURFACE_AREA", "DIAGONAL"])
            if l11 == "VOLUME":
                p9, q9 ,z9 = st.columns(3)
                xyz = p9.number_input("enter the value of length", 1.0, 1000.0, step=1.0)
                yzk = q9.number_input("enter the value of width", 1.0, 1000.0, step=1.0)
                zzz = z9.number_input("enter the value of higth", 1.0, 1000.0, step=1.0)
                vol5 = xyz * yzk * zzz  # formula of volume
                if st.button("check"):
                    st.write("VOLUME =", vol5)
                    st.balloons()
                    st.write("is it helpfull")
                if st.button("yes"):
                    st.write("thank you")
                    st.snow()
                elif st.button("no"):
                    st.write("we'll improve") # this is for AREA

            elif l11 == "SURFACE_AREA":
                rrr1, qqq1 ,sss = st.columns(3)
                ml = rrr1.number_input("enter the value of length", 1.0, 1000.0, step=1.0)
                lm = qqq1.number_input("enter the value of width", 1.0, 1000.0, step=1.0)
                cp = sss.number_input("enter the value of hight", 1.0, 1000.0, step=1.0)
                sr_ar = 2 * ( ml * lm + ml * cp + lm * cp) # formula of perimeter
                if st.button("check"):
                    st.write("PERIMETER =", sr_ar)
                    st.balloons()
                    st.write("is it helpfull")
                if st.button("yes"):
                    st.write("thank you")
                    st.snow()
                elif st.button("no"):
                    st.write("we'll improve") #this is for perimeter

            elif l11 == "DIAGONAL":
                r15, q15,s18 = st.columns(3)
                x96 = r15.number_input("enter the value of length", 1.0, 1000.0, step=1.0)
                z17 = q15.number_input("enter the value of width", 1.0, 1000.0, step=1.0)
                f9 = s18.number_input("enter the value of hight", 1.0, 1000.0, step=1.0)
                diao_cub = ( x96 * x96 + z17 * z17 + f9 * f9) # formula of diagonal
                if st.button("check"):
                    st.write("DIAGONAL =", diao_cub)
                    st.balloons()
                    st.write("is it helpfull")
                if st.button("yes"):
                    st.write("thank you")
                    st.snow()
                elif st.button("no"):
                    st.write("we'll improve")

