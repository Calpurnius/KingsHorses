from p4a.loadout import Crate

class cdf_explosives(Crate):
	title = 'CDF Explosives and CSW'
 	base = 'VTN_WPNE_LMG_BOX'
	weapons = [
		['VTN_SP81', 50],
		['VTN_RSP30_RED', 100],
		['VTN_RSP30_GREEN', 100],
		['VTN_RSP30_WHITE', 100],
	]
	magazines = [
		['VTN_OP_1k_WHITE', 100],
		['VTN_SP_1k_WHITE', 100],
		['VTN_SP_1k_RED', 100],
		['VTN_SP_1k_GREEN', 100],
		['VTN_SP_1k_YELLOW', 100],
		
		['rhs_mag_rdg2_white', 100],
		['rhs_mag_rdg2_black', 100],

		['VTN_NSPD', 100],
		['VTN_NSP_RED', 100],
		['VTN_NSP_YELLOW', 100],
		['VTN_NSP_GREEN', 100],
		['rhs_mine_tm62m_mag', 100],

		['VTN_VOG25', 100],
		['VTN_VOG25P', 100],
		['VTN_VG40MD', 100],
		['VTN_VG40OP', 100],
		['VTN_VGS401', 100],
		['VTN_VGS402', 100],
	]

	backpacks = [
		['RHS_NSV_Gun_Bag', 10],
		['RHS_NSV_Gun_Bag', 10],
		
		['RDS_DShkM_Gun_Bag', 10],
		['RDS_DShkM_TripodLow_Bag', 10],
		
		['RDS_Metis_Gun_Bag', 10],
		['RDS_Metis_Tripod_Bag', 10],

		['RDS_AGS30_Gun_Bag', 10],
		['RDS_AGS30_Tripod_Bag', 10],

		['RDS_SPG9_Gun_Bag', 10],
		['RDS_SPG9_Tripod_Bag', 10],
	]

class cdf_launchers(Crate):
	title = 'CDF Launchers and Warheads'
 	base = 'VTN_WPNE_SN_BOX'
	weapons = [
		['rhs_weap_rpg7', 10],
		['rhs_weap_rpg26', 100],
		['rhs_weap_rshg2', 50],
	]
	magazines = [
		['rhs_rpg7_PG7VL_mag', 100],
		['rhs_rpg7_PG7VR_mag', 100],
		['rhs_rpg7_OG7V_mag', 100],
	]

class cdf_weapons(Crate):
	title = 'CDF Rifles and Ammo'
 	base = 'VTN_WPNE_LMG_BOX'
	weapons = [
		['VTN_AK74_76', 10],
		['VTN_AKM', 10],
		['VTN_AK74_GP25', 5],
		['VTN_AKS74U_B', 5],
		['VTN_PKM', 5],
	]
	magazines = [
		['VTN_AK74_30b_SC', 500],
		['VTN_AK74_30b_TRC', 500],
		['VTN_AKM_30b_SC', 500],
		['VTN_AKM_30b_TRC', 500],
		['VTN_PK_100s_SC', 200],
		['VTN_PK_100s_TRC', 200],
	]

