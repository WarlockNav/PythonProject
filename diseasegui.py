import numpy as np
import pandas as pd
import csv
from sklearn import svm
from tkinter import *

data = pd.read_csv('manualTesting.csv')
F = data['prognosis']

symptoms = ['itching','skin_rash','nodal_skin_eruptions','continuous_sneezing','shivering',
            'chills','joint_pain','stomach_pain','acidity','ulcers_on_tongue','muscle_wasting','vomiting',
            'burning_micturition','spotting_urination','fatigue','weight_gain','anxiety','cold_hands_and_feets',
            'mood_swings','weight_loss','restlessness','lethargy','patches_in_throat','irregular_sugar_level',
            'cough','high_fever','sunken_eyes','breathlessness','sweating','dehydration','indigestion','headache',
            'yellowish_skin','dark_urine','nausea','loss_of_appetite','pain_behind_the_eyes','back_pain',
            'constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
            'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',
            'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
            'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs',
            'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',
            'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',
            'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
            'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',
            'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints',
            'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness',
            'weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of_urine',
            'continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
            'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
            'abnormal_menstruation','dischromic_patches','watering_from_eyes','increased_appetite',
            'polyuria','family_history','mucoid_sputum','rusty_sputum','lack_of_concentration',
            'visual_disturbances','receiving_blood_transfusion','receiving_unsterile_injections',
            'coma','stomach_bleeding','distention_of_abdomen','history_of_alcohol_consumption',
            'fluid_overload','blood_in_sputum','prominent_veins_on_calf','palpitations','painful_walking',
            'pus_filled_pimples','blackheads','scurring','skin_peeling','silver_like_dusting',
    'small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose','yellow_crust_ooze']


X1=data['itching']
X2=data['skin_rash']
X3=data['nodal_skin_eruptions']
X4=data['continuous_sneezing']
X5=data['shivering']
X6=data['chills']
X7=data['joint_pain']
X8=data['stomach_pain']
X9=data['acidity']
X10=data['ulcers_on_tongue']
X11=data['muscle_wasting']
X12=data['vomiting']
X13=data['burning_micturition']
X14=data['spotting_urination']
X15=data['fatigue']
X16=data['weight_gain']
X17=data['anxiety']
X18=data['cold_hands_and_feets']
X19=data['mood_swings']
X20=data['weight_loss']
X21=data['restlessness']
X22=data['lethargy']
X23=data['patches_in_throat']
X24=data['irregular_sugar_level']
X25=data['cough']
X26=data['high_fever']
X27=data['sunken_eyes']
X28=data['breathlessness']
X29=data['sweating']
X30=data['dehydration']
X31=data['indigestion']
X32=data['headache']
X33=data['yellowish_skin']
X34=data['dark_urine']
X35=data['nausea']
X36=data['loss_of_appetite']
X37=data['pain_behind_the_eyes']
X38=data['back_pain']
X39=data['constipation']
X40=data['abdominal_pain']
X41=data['diarrhoea']
X42=data['mild_fever']
X43=data['yellow_urine']
X44=data['yellowing_of_eyes']
X45=data['acute_liver_failure']
X46=data['fluid_overload']
X47=data['swelling_of_stomach']
X48=data['swelled_lymph_nodes']
X49=data['malaise']
X50=data['blurred_and_distorted_vision']
X51=data['phlegm']
X52=data['throat_irritation']
X53=data['redness_of_eyes']
X54=data['sinus_pressure']
X55=data['runny_nose']
X56=data['congestion']
X57=data['chest_pain']
X58=data['weakness_in_limbs']
X59=data['fast_heart_rate']
X60=data['pain_during_bowel_movements']
X61=data['pain_in_anal_region']
X62=data['bloody_stool']
X63=data['irritation_in_anus']
X64=data['neck_pain']
X65=data['dizziness']
X66=data['cramps']
X67=data['bruising']
X68=data['obesity']
X69=data['swollen_legs']
X70=data['swollen_blood_vessels']
X71=data['puffy_face_and_eyes']
X72=data['enlarged_thyroid']
X73=data['brittle_nails']
X74=data['swollen_extremeties']
X75=data['excessive_hunger']
X76=data['extra_marital_contacts']
X77=data['drying_and_tingling_lips']
X78=data['slurred_speech']
X79=data['knee_pain']
X80=data['hip_joint_pain']
X81=data['muscle_weakness']
X82=data['stiff_neck']
X83=data['swelling_joints']
X84=data['movement_stiffness']
X85=data['spinning_movements']
X86=data['loss_of_balance']
X87=data['unsteadiness']
X88=data['weakness_of_one_body_side']
X89=data['loss_of_smell']
X90=data['bladder_discomfort']
X91=data['foul_smell_of_urine']
X92=data['continuous_feel_of_urine']
X93=data['passage_of_gases']
X94=data['internal_itching']
X95=data['toxic_look_(typhos)']
X96=data['depression']
X97=data['irritability']
X98=data['muscle_pain']
X99=data['altered_sensorium']
X100=data['red_spots_over_body']
X101=data['belly_pain']
X102=data['abnormal_menstruation']
X103=data['dischromic_patches']
X104=data['watering_from_eyes']
X105=data['increased_appetite']
X106=data['polyuria']
X107=data['family_history']
X108=data['mucoid_sputum']
X109=data['rusty_sputum']
X110=data['lack_of_concentration']
X111=data['visual_disturbances']
X112=data['receiving_blood_transfusion']
X113=data['receiving_unsterile_injections']
X114=data['coma']
X115=data['stomach_bleeding']
X116=data['distention_of_abdomen']
X117=data['history_of_alcohol_consumption']
X118=data['fluid_overload']
X119=data['blood_in_sputum']
X120=data['prominent_veins_on_calf']
X121=data['palpitations']
X122=data['painful_walking']
X123=data['pus_filled_pimples']
X124=data['blackheads']
X125=data['scurring']
X126=data['skin_peeling']
X127=data['silver_like_dusting']
X128=data['small_dents_in_nails']
X129=data['inflammatory_nails']
X130=data['blister']
X131=data['red_sore_around_nose']
X132=data['yellow_crust_ooze']

#print(X124)

p=(X1,X2,X3,X4,X5,X6,X7,X8,X9,X10,X11,X12,X13,X14,X15,X16,X17,X18,X19,X20,X21,X22,X23,X24,X25,X26,X27,X28,X29,X30,X31,X32,X33,X34,X35,X36,X37,X38,X39,X40,
   X41,X42,X43,X44,X45,X46,X47,X48,X49,X50,X51,X52,X53,X54,X55,X56,X57,X58,X59,X60,X61,X62,X63,X64,X65,X66,X67,X68,X69,X70,
   X71,X72,X73,X74,X75,X76,X77,X78,X79,X80,X81,X82,X83,X84,X85,X86,X87,X88,X89,X90,X91,X92,X93,X94,X95,X96,X97,X98,X99,X100,
   X101,X102,X103,X104,X105,X106,X107,X108,X109,X110,X111,X112,X113,X114,X115,X116,X117,X118,X119,X120,X121,X122,X123,X124,X125,X126,X127,X128,X129,X130,X131,X132)

Features=[]
Lables=[]

for i in range(0,len(X1)):
    a1 = X1[i]
    a2 = X2[i]
    a3 = X3[i]
    a4 = X4[i]
    a5 = X5[i]
    a6 = X6[i]
    a7 = X7[i]
    a8 = X8[i]
    a9 = X9[i]
    a10 = X10[i]
    a11 =X11[i]
    a12=X12[i]
    a13=X13[i]
    a14=X14[i]
    a15=X15[i]
    a16=X16[i]
    a17=X17[i]
    a18=X18[i]
    a19=X19[i]
    a20=X20[i]
    a21=X21[i]
    a22=X22[i]
    a23=X23[i]
    a24=X24[i]
    a25=X25[i]
    a26=X26[i]
    a27=X27[i]
    a28=X28[i]
    a29=X29[i]
    a30=X30[i]
    a31=X31[i]
    a32=X32[i]
    a33=X33[i]
    a34=X34[i]
    a35=X35[i]
    a36=X36[i]
    a37=X37[i]
    a38=X38[i]
    a39=X39[i]
    a40=X40[i]
    a41=X41[i]
    a42=X42[i]
    a43=X43[i]
    a44=X44[i]
    a45=X45[i]
    a46=X46[i]
    a47=X47[i]
    a48=X48[i]
    a49=X49[i]
    a50=X50[i]
    a51=X51[i]
    a52=X52[i]
    a53=X53[i]
    a54=X54[i]
    a55=X55[i]
    a56=X56[i]
    a57=X57[i]
    a58=X58[i]
    a59=X59[i]
    a60=X60[i]
    a61=X61[i]
    a62=X62[i]
    a63=X63[i]
    a64=X64[i]
    a65=X65[i]
    a66=X66[i]
    a67=X67[i]
    a68=X68[i]
    a69=X69[i]
    a70=X70[i]
    a71=X71[i]
    a72=X72[i]
    a73=X73[i]
    a74=X74[i]
    a75=X75[i]
    a76=X76[i]
    a77=X77[i]
    a78=X78[i]
    a79=X79[i]
    a80=X80[i]
    a81=X81[i]
    a82=X82[i]
    a83=X83[i]
    a84=X84[i]
    a85=X85[i]
    a86=X86[i]
    a87=X87[i]
    a88=X88[i]
    a89=X89[i]
    a90=X90[i]
    a91=X91[i]
    a92=X92[i]
    a93=X93[i]
    a94=X94[i]
    a95=X95[i]
    a96=X96[i]
    a97=X97[i]
    a98=X98[i]
    a99=X99[i]
    a100=X100[i]
    a101=X101[i]
    a102=X102[i]
    a103=X103[i]
    a104=X104[i]
    a105=X105[i]
    a106=X106[i]
    a107=X107[i]
    a108=X108[i]
    a109=X109[i]
    a110=X110[i]
    a111=X111[i]
    a112=X112[i]
    a113=X113[i]
    a114=X114[i]
    a115=X115[i]
    a116=X116[i]
    a117=X117[i]
    a118=X118[i]
    a119=X119[i]
    a120=X120[i]
    a121=X121[i]
    a122=X122[i]
    a123=X123[i]
    a124=X124[i]
    a125=X125[i]
    a126=X126[i]
    a127=X127[i]
    a128=X128[i]
    a129=X129[i]
    a130=X130[i]
    a131=X131[i]
    a132=X132[i]
    f = F[i]
    e = (a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26,a27,a28,a29,a30,a31,a32,a33,a34,a35,a36,a37,a38,a39,a40,
         a41,a42,a43,a44,a45,a46,a47,a48,a49,a50,a51,a52,a53,a54,a55,a56,a57,a58,a59,a60,a61,a62,a63,a64,a65,a66,a67,a68,a69,a70,a71,a72,a73,a74,a75,a76,a77,a78,a79,a80,
         a81,a82,a83,a84,a85,a86,a87,a88,a89,a90,a91,a92,a93,a94,a95,a96,a97,a98,a99,a100,a101,a102,a103,a104,a105,a106,a107,a108,a109,a110,a111,a112,a113,a114,a115,a116,a117,a118,a119,a120,
         a121,a122,a123,a124,a125,a126,a127,a128,a129,a130,a131,a132)
    Features.append(e)
    Lables.append(f)


def onClick():
    print("Button Clicked")
    sym1 = entrysym1.get()
    sym2 = entrysym2.get()
    sym3 = entrysym3.get()

    sym4 = entrysym4.get()
    #points = entrypoints.get()
    #sym5 = entrysym5.get()
    print(sym1,sym2,sym3,sym4)
    a = (sym1,sym2,sym3,sym4)
    b = []
    c = []
    for i in range(0, len(symptoms)):
        c.append(0)
    for i in range(0, len(symptoms)):
        for j in range(0, len(a)):
            if a[j] == symptoms[i]:
                # c.append(a[j])
                b.append(i)
    for i in range(0, len(b)):
        j = b[i]
        c[j] = 1
    #print(c)

    clf = svm.SVC(gamma='scale')
    clf.fit(Features, Lables)
    output = clf.predict([(c)])
    print(output)


window = Tk()
lblTitle = Label(window, text="Enter symptoms Below:")
lblTitle.pack()

lblsym1 = Label(window, text="Enter Symptom 1:")
lblsym1.pack()

entrysym1 = Entry(window)
entrysym1.pack()

lblsym2 = Label(window, text="Enter Symptom 2:")
lblsym2.pack()

entrysym2 = Entry(window)
entrysym2.pack()

lblsym3 = Label(window, text="Enter Symptom 3:")
lblsym3.pack()

entrysym3 = Entry(window)
entrysym3.pack()

lblsym4 = Label(window, text="Enter Symptom 4:")
lblsym4.pack()

entrysym4 = Entry(window)
entrysym4.pack()

btnAddsymptom = Button(window, text="Submit", command=onClick)
btnAddsymptom.pack()
window.mainloop()
