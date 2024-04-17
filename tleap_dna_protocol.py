tleap protocol ####################################################################################################################
Inspired by https://amberhub.chpc.utah.edu/analisis-of-nucleic-acid-simulation/

use tleap to prepare your pdb file in the correct amber format:

module purge
module load cpu/0.17.3b  gcc/10.2.0/npcyll4  openmpi/4.1.3/oq3qvsv amber/22
tleap -f $AMBERHOME/dat/leap/cmd/leaprc.DNA.bsc1 #in this case this forcefield is for DNA
  source leaprc.protein.ff14SB #I will consider this for proteins, only necessary if you will load proteins 
  source leaprc.water.tip3p #and water
#use the command >list 
#this command will show all the elements that are considered in the system, for example check if all DNA bases are there, proteins that are in our system
#for example 
                                        > list
                                        ACE       AG        AL        ALA       ARG       ASH       ASN       ASP
                                        Ag        BA        BR        Be        CA        CALA      CARG      CASN
                                        CASP      CCYS      CCYX      CD        CE        CGLN      CGLU      CGLY
                                        CHCL3BOX  CHID      CHIE      CHIP      CHIS      CHYP      CILE      CL
                                        CLEU      CLYS      CMET      CO        CPHE      CPRO      CR        CS
                                        CSER      CTHR      CTRP      CTYR      CU        CU1       CVAL      CYM
                                        CYS       CYX       Ce        Cl-       Cr        DA        DA3       DA5
                                        DAN       DC        DC3       DC4       DC5       DCN       DG        DG3
                                        DG5       DGN       DT        DT3       DT5       DTN       Dy        EU
                                        EU3       Er        F         FB3       FB3BOX    FB4       FB4BOX    FE
                                        FE2       GD3       GLH       GLN       GLU       GLY       H3O+      HE+
                                        HG        HID       HIE       HIP       HIS       HOH       HYP       HZ+
                                        Hf        ILE       IN        IOD       K         K+        LA        LEU
                                        LI        LU        LYN       LYS       MEOHBOX   MET       MG        MN
                                        NA        NALA      NARG      NASN      NASP      NCYS      NCYX      NGLN
                                        NGLU      NGLY      NH4       NHE       NHID      NHIE      NHIP      NHIS
                                        NI        NILE      NLEU      NLYS      NMABOX    NME       NMET      NPHE
                                        NPRO      NSER      NTHR      NTRP      NTYR      NVAL      Na+       Nd
                                        O3P       OP3       OPC       OPC3BOX   OPCBOX    PB        PD        PHE
                                        PL3       POL3BOX   PR        PRO       PT        Pu        QSPCFWBOX RB
                                        Ra        SER       SM        SPC       SPCBOX    SPCFWBOX  SPF       SPG
                                        SR        Sm        Sn        T4E       TB        THR       TIP3PBOX  TIP3PFBOX
                                        TIP4PBOX  TIP4PEWBOXTIP5PBOX  TL        TP3       TP4       TP5       TPF
                                        TRP       TYR       Th        Tl        Tm        U4+       V2+       VAL
                                        WAT       Y         YB2       ZN        Zr        dna1      frcmod14SB
                                        >
dna1= loadpdb "1bna.pdb" #loads the pdb file

  Loading PDB file: ./1bna.pdb
            (starting new molecule for chain B)
            total atoms in file: 566
            Leap added 432 missing atoms according to residue templates:
                432 H / lone pairs
                
saveamberparm dna1 1bna.prmtop 1bna.crdbox #this saves the coordinates and topology of the file
            Warning: The unperturbed charge of the unit (-22.000000) is not zero.

            Note: Ignoring the warning from Unit Checking.

            Building topology.
            Building atom parameters.
            Building bond parameters.
            Building angle parameters.
            Building proper torsion parameters.
            Building improper torsion parameters.
            total 164 improper torsions applied
            Building H-Bond parameters.
            Incorporating Non-Bonded adjustments.
            Not Marking per-residue atom chain types.
            Marking per-residue atom chain types.
            (Residues lacking connect0/connect1 -
            these don't have chain types marked:

                    res     total affected

                    WAT     80
            )
            (no restraints)
            
            

            
~/scripts/amber2bgf.pl [prmtop] [crdbox] [name_of_bgf_file_to_create]
~/scripts/amber2bgf.pl 1bna.prmtop 1bna.rst7 1bna.bgf #joins the files into a bgf file

