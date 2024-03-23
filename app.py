import streamlit as st
import pandas as pd
import numpy as np
import pickle


# Load the trained Decision Tree model
model = pickle.load(open('decision_tree_model.pkl', 'rb'))



# Streamlit app
st.title('House Price Prediction')

    # 1 MSSubClass: Identifies the type of dwelling involved in the sale
mssubclass_options = [20,30,40,45,50,60,70,75,80,85,90,120,150,160,180,190]
mssubclass = st.selectbox("MSSubClass:", mssubclass_options)





# 4 LotArea: Lot size in square feet
lot_area = st.number_input("LotArea:", min_value=0)

# 5 
print("Street: Type of road access to property Grvl = 1, Pave = 2")
street_options = [1, 2]
street = st.selectbox("Street:", street_options)



# 7 LotShape: General shape of property
lot_shape_options = ["Reg", "IR1", "IR2", "IR3"]
lot_shape = st.selectbox("LotShape:", lot_shape_options)

# 8 LandContour: Flatness of the property
land_contour_options = ["Lvl", "Bnk",
                        "HLS", "Low"]
land_contour = st.selectbox("LandContour:", land_contour_options)



# 10 LotConfig: Lot configuration
lot_config_options = ["Inside", "Corner", " CulDSac", "FR2",
                    "FR3"]
lot_config = st.selectbox("LotConfig:", lot_config_options)

# 11 LandSlope: Slope of property
land_slope_options = ["Gtl", "Mod", "Sev"]
land_slope = st.selectbox("LandSlope:", land_slope_options)
# 12 Neighborhood: Physical locations within Ames city limits
neighborhood_options = {"Blmngtn","Blueste","BrDale","BrkSide","ClearCr","CollgCr","Crawfor","Edwards","Gilbert","IDOTRR","MeadowV","Mitchel","Names","NoRidge","NPkVill","NridgHt","NWAmes","OldTown","SWISU","Sawyer","SawyerW","Somerst","StoneBr","Timber","Veenker"}
neighborhood = st.selectbox("Neighborhood : ",neighborhood_options);

condition1_options = ["Artery", "Feedr", "Norm", "RRNn", "RRAn", "PosN", "PosA", "RRNe", "RRAe"]
condition1 = st.selectbox("Proximity to various conditions:", condition1_options)

condition2_options = ["Artery", "Feedr", "Norm", "RRNn", "RRAn", "PosN", "PosA", "RRNe", "RRAe"]
condition2 = st.selectbox("Proximity to various conditions (if more than one is present):", condition2_options)

bldg_type_options = ["1Fam", "2FmCon", "Duplx", "TwnhsE", "TwnhsI"]
bldg_type = st.selectbox("Type of dwelling:", bldg_type_options)

house_style_options = ["1Story", "1.5Fin", "1.5Unf", "2Story", "2.5Fin", "2.5Unf", "SFoyer", "SLvl"]
house_style = st.selectbox("Style of dwelling:", house_style_options)

overall_quality_options = list(range(1, 11))
overall_quality = st.selectbox("Overall Quality (1-10):", overall_quality_options)

overall_condition_options = list(range(1, 11))
overall_condition = st.selectbox("Overall Condition (1-10):", overall_condition_options)

year_built_options = list(range(1800, 2026))
year_built = st.selectbox("Year Built:", year_built_options)

year_remodel_add_options = list(range(1800, 2026))
year_remodel_add = st.selectbox("Year Remodel/Add:", year_remodel_add_options)

# 21 RoofStyle: Type of roof
roof_style_options = ["Flat", "Gable", "Gambrel", "Hip", "Mansard", "Shed"]
roof_style = st.selectbox("Roof Style:", roof_style_options)

roof_material_options = ["ClyTile", "CompShg", "Membran", "Metal", "Roll", "Tar&Grv", "WdShake", "WdShngl"]
roof_material = st.selectbox("Roof Material:", roof_material_options)

exterior_1st_options = ["AsbShng", "AsphShn", "BrkComm", "BrkFace", "CBlock", "CemntBd", "HdBoard", "ImStucc", "MetalSd",
                        "Other", "Plywood", "PreCast", "Stone", "Stucco", "VinylSd", "Wd Sdng", "WdShing"]
exterior_1st = st.selectbox("Exterior covering on house:", exterior_1st_options)

exterior_2nd_options = ["AsbShng", "AsphShn", "BrkComm", "BrkFace", "CBlock", "CemntBd", "HdBoard", "ImStucc", "MetalSd",
                        "Other", "Plywood", "PreCast", "Stone", "Stucco", "VinylSd", "Wd Sdng", "WdShing"]
exterior_2nd = st.selectbox("Exterior covering on house (if more than one material):", exterior_2nd_options)


exter_qual_options = ["Ex", "Gd", "TA", "Fa", "Po"]
exter_qual = st.selectbox("Exterior Quality:", exter_qual_options)

exter_cond_options = ["Ex", "Gd", "TA", "Fa", "Po"]
exter_cond = st.selectbox("Exterior Condition:", exter_cond_options)

foundation_options = ["BrkTil", "CBlock", "PConc", "Slab", "Stone", "Wood"]
foundation = st.selectbox("Foundation Type:", foundation_options)



heating_options = ["Floor", "GasA", "GasW", "Grav", "OthW", "Wall"]
heating = st.selectbox("Heating:", heating_options)

heating_qc_options = ["Ex", "Gd", "TA", "Fa", "Po"]
heating_qc = st.selectbox("Heating Quality and Condition:", heating_qc_options)

central_air_options = ["N", "Y"]
central_air = st.selectbox("Central Air Conditioning:", central_air_options)

low_quality_fin_sf = st.number_input("LowQualFinSF", min_value=0)


above_grade_living_area_sf = st.number_input("GrLivArea", min_value=0)



# FullBath: Full bathrooms above grade
full_bath = st.number_input("FullBath", min_value=0)

# HalfBath: Half baths above grade
half_bath = st.number_input("HalfBath", min_value=0)

# Bedroom: Bedrooms above grade (does NOT include basement bedrooms)
bedrooms = st.number_input("Bedroom", min_value=0)

# Kitchen: Kitchens above grade
kitchens = st.number_input("Kitchen", min_value=0)


# TotRmsAbvGrd: Total rooms above grade (does not include bathrooms)
total_rooms_above_grade = st.number_input("TotRmsAbvGrd", min_value=0)



# Fireplaces: Number of fireplaces
fireplaces = st.number_input("Fireplaces", min_value=0)



# PavedDrive: Paved driveway
paved_drive_options = ["Y", "P", "N"]
paved_drive = st.selectbox("PavedDrive", paved_drive_options)

# WoodDeckSF: Wood deck area in square feet
wood_deck_sf = st.number_input("WoodDeckSF", min_value=0)

# OpenPorchSF: Open porch area in square feet
open_porch_sf = st.number_input("OpenPorchSF", min_value=0)

# EnclosedPorch: Enclosed porch area in square feet
enclosed_porch_sf = st.number_input("EnclosedPorch", min_value=0)

# 3SsnPorch: Three season porch area in square feet
three_season_porch_sf = st.number_input("3SsnPorch", min_value=0)

# ScreenPorch: Screen porch area in square feet
screen_porch_sf = st.number_input("ScreenPorch", min_value=0)

# PoolArea: Pool area in square feet
pool_area = st.number_input("PoolArea", min_value=0)


misc_value = st.number_input("MiscVal", min_value=0)

# MoSold: Month Sold (MM)
month_sold = st.number_input("MoSold", min_value=1, max_value=12)

# YrSold: Year Sold (YYYY)
year_sold = st.number_input("YrSold", min_value=0)



# SaleCondition: Condition of sale
sale_condition_options = ["Normal", "Abnorml", "AdjLand", "Alloca", "Family", "Partial"]
sale_condition = st.selectbox("SaleCondition", sale_condition_options)

print("check");


# Tạo bản đồ ánh xạ cho các lựa chọn

# lot_shape_mapping
lot_shape_mapping = {"Reg": 0, "IR1": 1, "IR2": 2, "IR3": 3}

# land_contour_mapping
land_contour_mapping = {"Lvl": 0, "Bnk": 1, "HLS": 2, "Low": 3}

# lot_config_mapping
lot_config_mapping = {"Inside": 0, "Corner": 1, "CulDSac": 2, "FR2": 3, "FR3": 4}

# land_slope_mapping
land_slope_mapping = {"Gtl": 0, "Mod": 1, "Sev": 2}

# neighborhood_mapping
neighborhood_mapping = {"Blmngtn": 0, "Blueste": 1, "BrDale": 2, "BrkSide": 3, "ClearCr": 4, "CollgCr": 5,
                        "Crawfor": 6, "Edwards": 7, "Gilbert": 8, "IDOTRR": 9, "MeadowV": 10, "Mitchel": 11,
                        "Names": 12, "NoRidge": 13, "NPkVill": 14, "NridgHt": 15, "NWAmes": 16, "OldTown": 17,
                        "SWISU": 18, "Sawyer": 19, "SawyerW": 20, "Somerst": 21, "StoneBr": 22, "Timber": 23,
                        "Veenker": 24}

# condition1_mapping
condition1_mapping = {"Artery": 0, "Feedr": 1, "Norm": 2, "RRNn": 3, "RRAn": 4, "PosN": 5, "PosA": 6, "RRNe": 7, "RRAe": 8}

# condition2_mapping
condition2_mapping = {"Artery": 0, "Feedr": 1, "Norm": 2, "RRNn": 3, "RRAn": 4, "PosN": 5, "PosA": 6, "RRNe": 7, "RRAe": 8}

# bldg_type_mapping
bldg_type_mapping = {"1Fam": 0, "2FmCon": 1, "Duplx": 2, "TwnhsE": 3, "TwnhsI": 4}

# house_style_mapping
house_style_mapping = {"1Story": 0, "1.5Fin": 1, "1.5Unf": 2, "2Story": 3, "2.5Fin": 4, "2.5Unf": 5, "SFoyer": 6, "SLvl": 7}

# exter_qual_mapping
exter_qual_mapping = {"Ex": 0, "Gd": 1, "TA": 2, "Fa": 3, "Po": 4}

# exter_cond_mapping
exter_cond_mapping = {"Ex": 0, "Gd": 1, "TA": 2, "Fa": 3, "Po": 4}

# foundation_mapping
foundation_mapping = {"BrkTil": 0, "CBlock": 1, "PConc": 2, "Slab": 3, "Stone": 4, "Wood": 5}

# heating_mapping
heating_mapping = {"Floor": 0, "GasA": 1, "GasW": 2, "Grav": 3, "OthW": 4, "Wall": 5}

# heating_qc_mapping
heating_qc_mapping = {"Ex": 0, "Gd": 1, "TA": 2, "Fa": 3, "Po": 4}

# central_air_mapping
central_air_mapping = {"N": 0, "Y": 1}

# paved_drive_mapping
paved_drive_mapping = {"Y": 0, "P": 1, "N": 2}

# sale_condition_mapping
sale_condition_mapping = {"Normal": 0, "Abnorml": 1, "AdjLand": 2, "Alloca": 3, "Family": 4, "Partial": 5}

# roof_style_mapping
roof_style_mapping = {"Flat": 0, "Gable": 1, "Gambrel": 2, "Hip": 3, "Mansard": 4, "Shed": 5}

# roof_material_mapping
roof_material_mapping = {"ClyTile": 0, "CompShg": 1, "Membran": 2, "Metal": 3, "Roll": 4, "Tar&Grv": 5, "WdShake": 6, "WdShngl": 7}

exterior1_mapping = {exterior: index + 1 for index, exterior in enumerate(exterior_1st_options)}

exterior2_mapping = {exterior: index + 1 for index, exterior in enumerate(exterior_2nd_options)}

# Ánh xạ giá trị từ các lựa chọn sang số

# alley = alley_mapping[alley]
lot_shape = lot_shape_mapping[lot_shape]
land_contour = land_contour_mapping[land_contour]
lot_config = lot_config_mapping[lot_config]
land_slope = land_slope_mapping[land_slope]
neighborhood = neighborhood_mapping[neighborhood]
condition1 = condition1_mapping[condition1]
condition2 = condition2_mapping[condition2]
bldg_type = bldg_type_mapping[bldg_type]
house_style = house_style_mapping[house_style]
exter_qual = exter_qual_mapping[exter_qual]
exter_cond = exter_cond_mapping[exter_cond]
foundation = foundation_mapping[foundation]
heating = heating_mapping[heating]
heating_qc = heating_qc_mapping[heating_qc]
central_air = central_air_mapping[central_air]
paved_drive = paved_drive_mapping[paved_drive]
sale_condition = sale_condition_mapping[sale_condition]
roof_style = roof_style_mapping[roof_style]
roof_material = roof_material_mapping[roof_material]
exterior_1st = exterior1_mapping[exterior_1st]
exterior_2nd = exterior2_mapping[exterior_2nd]





# Tạo một từ điển để ánh xạ giữa tùy chọn văn bản và giá trị số




# Mã hóa giá trị được chọn sang giá trị số tương ứng



# 1. Tạo dữ liệu đầu vào cho mô hình
input_data = {
'Street': street, 'LotShape': lot_shape, 'LandContour':land_contour, 'LotConfig':lot_config, 'LandSlope':land_slope,
    'Neighborhood': neighborhood, 'Condition1': condition1, 'Condition2':condition2, 'BldgType':bldg_type, 'HouseStyle':house_style,
    'RoofStyle': roof_style, 'RoofMatl': roof_material, 'ExterQual':exter_qual, 'ExterCond': exter_cond, 'Foundation':foundation,
    'Heating': heating, 'HeatingQC':heating_qc, 'CentralAir':central_air, 'PavedDrive':paved_drive, 'SaleCondition':sale_condition,
    'MSSubClass':mssubclass, 'LotArea':lot_area, 'OverallQual':overall_quality, 'OverallCond':overall_condition, 'YearBuilt':year_built,
    'YearRemodAdd':year_remodel_add, '1stFlrSF': exterior_1st, '2ndFlrSF':exterior_2nd, 'LowQualFinSF':low_quality_fin_sf, 'GrLivArea':above_grade_living_area_sf,
    'FullBath':full_bath, 'HalfBath':half_bath, 'BedroomAbvGr':bedrooms, 'KitchenAbvGr':kitchens, 'TotRmsAbvGrd':total_rooms_above_grade,
    'Fireplaces':fireplaces, 'WoodDeckSF':wood_deck_sf, 'OpenPorchSF':open_porch_sf, 'EnclosedPorch':enclosed_porch_sf, '3SsnPorch':three_season_porch_sf,
    'ScreenPorch':screen_porch_sf, 'PoolArea':pool_area, 'MiscVal':misc_value, 'MoSold':month_sold, 'YrSold':year_sold
}




input_df = pd.DataFrame([input_data])
# 2. Sử dụng mô hình để dự đoán
prediction = model.predict(input_df)

# 3. Xuất dự đoán ra giao diện người dùng
st.write("Dự đoán giá nhà của bạn là:", prediction[0])

# 4. Xuất dự đoán ra một tệp CSV
output_df = pd.DataFrame({'Prediction': prediction})
output_df.to_csv('house_price_prediction.csv', index=False)


