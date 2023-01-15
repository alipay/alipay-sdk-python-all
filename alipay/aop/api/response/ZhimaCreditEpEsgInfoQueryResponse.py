#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditEpEsgInfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpEsgInfoQueryResponse, self).__init__()
        self._bankrupt_liquid_12_m_flag = None
        self._emi_licen_ban_num_12_m_flag = None
        self._ep_abn_status_flag = None
        self._ep_adm_team_adj_num_12_m = None
        self._ep_big_tax_illegal_num_12_m = None
        self._ep_biggest_share_holder_ratio = None
        self._ep_bond_default_flag = None
        self._ep_bond_defaults_num_12_m = None
        self._ep_brand_add_num_12_m = None
        self._ep_busi_abnor_num_12_m = None
        self._ep_busi_abnor_top_type_12_m = None
        self._ep_busi_scope_adj_num_12_m = None
        self._ep_cert_no = None
        self._ep_cetificate_list = None
        self._ep_child_risk_12_m_flag = None
        self._ep_climate_risk_exp = None
        self._ep_co_2_emi_per_rvn = None
        self._ep_copyright_add_num_12_m = None
        self._ep_copyright_total_num = None
        self._ep_corrupt_brib_legal_case_num_12_m = None
        self._ep_criminal_case_num_12_m = None
        self._ep_down_rating_bond_num_12_m = None
        self._ep_down_rating_issuer_num_12_m = None
        self._ep_energy_consume_per_rvn = None
        self._ep_env_evaluate_12_m = None
        self._ep_env_evaluate_adj_12_m = None
        self._ep_env_legal_case_num_12_m = None
        self._ep_env_penalty_amt_12_m = None
        self._ep_env_penalty_num_12_m = None
        self._ep_env_penalty_top_type_12_m = None
        self._ep_fake_prop_penalty_num_12_m = None
        self._ep_fd = None
        self._ep_fire_penalty_amt_12_m = None
        self._ep_fire_penalty_num_12_m = None
        self._ep_fire_penalty_top_type_12_m = None
        self._ep_force_excute_num_12_m = None
        self._ep_founding_years = None
        self._ep_group = None
        self._ep_holder_eqty_frez_amt_12_m = None
        self._ep_holder_eqty_frez_num_12_m = None
        self._ep_holder_eqty_frez_ratio_12_m = None
        self._ep_holder_eqty_frez_ratio_12_m_new = None
        self._ep_holder_eqty_pledge_amt_12_m = None
        self._ep_holder_eqty_pledge_num_12_m = None
        self._ep_holder_eqty_pledge_ratio_12_m = None
        self._ep_hr_legal_case_num_12_m = None
        self._ep_hr_penalty_amt_12_m = None
        self._ep_hr_penalty_num_12_m = None
        self._ep_hr_penalty_top_type_12_m = None
        self._ep_hzd_penalty_num_12_m = None
        self._ep_hzd_penalty_top_type_12_m = None
        self._ep_icp_add_num_12_m = None
        self._ep_industry_lv_1_code = None
        self._ep_industry_lv_2_code = None
        self._ep_industry_lv_3_code = None
        self._ep_industry_lv_4_code = None
        self._ep_investor_eqty_adj_num_12_m = None
        self._ep_ip_legal_case_num_12_m = None
        self._ep_lastyear_ann_rpt_disclose_flag = None
        self._ep_latest_ann_rpt_audit_flag = None
        self._ep_latest_ann_rpt_audit_opinion = None
        self._ep_legal_person_adj_num_12_m = None
        self._ep_lost_credit_excute_num_12_m = None
        self._ep_lost_credit_hist_num_12_m = None
        self._ep_mom_risk_12_m_flag = None
        self._ep_name = None
        self._ep_nephew_risk_12_m_flag = None
        self._ep_oprt_scope = None
        self._ep_org_reg_cptl = None
        self._ep_org_reg_cptl_curcy = None
        self._ep_org_reg_time = None
        self._ep_org_status = None
        self._ep_other_legal_case_num_12_m = None
        self._ep_other_penalty_amt_12_m = None
        self._ep_other_penalty_num_12_m = None
        self._ep_other_penalty_top_type_12_m = None
        self._ep_patent_add_num_12_m = None
        self._ep_patent_total_num = None
        self._ep_private_lend_legal_case_num_12_m = None
        self._ep_qlty_penalty_amt_12_m = None
        self._ep_qlty_penalty_num_12_m = None
        self._ep_qlty_penalty_top_type_12_m = None
        self._ep_reg_addr = None
        self._ep_reg_cptl_adj_ratio_12_m = None
        self._ep_resource_other_dependence = None
        self._ep_resource_water_dependence = None
        self._ep_root_risk_12_m_flag = None
        self._ep_secu_penalty_amt_12_m = None
        self._ep_secu_penalty_num_12_m = None
        self._ep_secu_penalty_top_type_12_m = None
        self._ep_serious_illegal_list_flag = None
        self._ep_sibling_risk_12_m_flag = None
        self._ep_solid_emi_per_rvn = None
        self._ep_staff_num_adj_rate_12_m = None
        self._ep_status = None
        self._ep_tax_abnor_acct_num_12_m = None
        self._ep_tax_credit_adj_dic_latest = None
        self._ep_tax_penalty_amt_12_m = None
        self._ep_tax_penalty_num_12_m = None
        self._ep_tax_penalty_top_type_12_m = None
        self._ep_uncle_risk_12_m_flag = None
        self._ep_unfair_compt_legal_case_num_12_m = None
        self._evaluate_time = None
        self._excu_limi_high_consum_12_m_flag = None
        self._issue_green_bond_flag = None
        self._over_std_gas_emi_last_year_flag = None
        self._over_std_water_emi_last_year_flag = None
        self._over_vol_gas_emi_last_year_flag = None
        self._over_vol_water_emi_last_year_flag = None
        self._owing_tax_12_m_flag = None
        self._req_emi_adj_12_m_flag = None
        self._tax_as_pay_12_m_flag = None
        self._tax_credit_a_level_latest_flag = None

    @property
    def bankrupt_liquid_12_m_flag(self):
        return self._bankrupt_liquid_12_m_flag

    @bankrupt_liquid_12_m_flag.setter
    def bankrupt_liquid_12_m_flag(self, value):
        self._bankrupt_liquid_12_m_flag = value
    @property
    def emi_licen_ban_num_12_m_flag(self):
        return self._emi_licen_ban_num_12_m_flag

    @emi_licen_ban_num_12_m_flag.setter
    def emi_licen_ban_num_12_m_flag(self, value):
        self._emi_licen_ban_num_12_m_flag = value
    @property
    def ep_abn_status_flag(self):
        return self._ep_abn_status_flag

    @ep_abn_status_flag.setter
    def ep_abn_status_flag(self, value):
        self._ep_abn_status_flag = value
    @property
    def ep_adm_team_adj_num_12_m(self):
        return self._ep_adm_team_adj_num_12_m

    @ep_adm_team_adj_num_12_m.setter
    def ep_adm_team_adj_num_12_m(self, value):
        self._ep_adm_team_adj_num_12_m = value
    @property
    def ep_big_tax_illegal_num_12_m(self):
        return self._ep_big_tax_illegal_num_12_m

    @ep_big_tax_illegal_num_12_m.setter
    def ep_big_tax_illegal_num_12_m(self, value):
        self._ep_big_tax_illegal_num_12_m = value
    @property
    def ep_biggest_share_holder_ratio(self):
        return self._ep_biggest_share_holder_ratio

    @ep_biggest_share_holder_ratio.setter
    def ep_biggest_share_holder_ratio(self, value):
        self._ep_biggest_share_holder_ratio = value
    @property
    def ep_bond_default_flag(self):
        return self._ep_bond_default_flag

    @ep_bond_default_flag.setter
    def ep_bond_default_flag(self, value):
        self._ep_bond_default_flag = value
    @property
    def ep_bond_defaults_num_12_m(self):
        return self._ep_bond_defaults_num_12_m

    @ep_bond_defaults_num_12_m.setter
    def ep_bond_defaults_num_12_m(self, value):
        self._ep_bond_defaults_num_12_m = value
    @property
    def ep_brand_add_num_12_m(self):
        return self._ep_brand_add_num_12_m

    @ep_brand_add_num_12_m.setter
    def ep_brand_add_num_12_m(self, value):
        self._ep_brand_add_num_12_m = value
    @property
    def ep_busi_abnor_num_12_m(self):
        return self._ep_busi_abnor_num_12_m

    @ep_busi_abnor_num_12_m.setter
    def ep_busi_abnor_num_12_m(self, value):
        self._ep_busi_abnor_num_12_m = value
    @property
    def ep_busi_abnor_top_type_12_m(self):
        return self._ep_busi_abnor_top_type_12_m

    @ep_busi_abnor_top_type_12_m.setter
    def ep_busi_abnor_top_type_12_m(self, value):
        self._ep_busi_abnor_top_type_12_m = value
    @property
    def ep_busi_scope_adj_num_12_m(self):
        return self._ep_busi_scope_adj_num_12_m

    @ep_busi_scope_adj_num_12_m.setter
    def ep_busi_scope_adj_num_12_m(self, value):
        self._ep_busi_scope_adj_num_12_m = value
    @property
    def ep_cert_no(self):
        return self._ep_cert_no

    @ep_cert_no.setter
    def ep_cert_no(self, value):
        self._ep_cert_no = value
    @property
    def ep_cetificate_list(self):
        return self._ep_cetificate_list

    @ep_cetificate_list.setter
    def ep_cetificate_list(self, value):
        if isinstance(value, list):
            self._ep_cetificate_list = list()
            for i in value:
                self._ep_cetificate_list.append(i)
    @property
    def ep_child_risk_12_m_flag(self):
        return self._ep_child_risk_12_m_flag

    @ep_child_risk_12_m_flag.setter
    def ep_child_risk_12_m_flag(self, value):
        self._ep_child_risk_12_m_flag = value
    @property
    def ep_climate_risk_exp(self):
        return self._ep_climate_risk_exp

    @ep_climate_risk_exp.setter
    def ep_climate_risk_exp(self, value):
        self._ep_climate_risk_exp = value
    @property
    def ep_co_2_emi_per_rvn(self):
        return self._ep_co_2_emi_per_rvn

    @ep_co_2_emi_per_rvn.setter
    def ep_co_2_emi_per_rvn(self, value):
        self._ep_co_2_emi_per_rvn = value
    @property
    def ep_copyright_add_num_12_m(self):
        return self._ep_copyright_add_num_12_m

    @ep_copyright_add_num_12_m.setter
    def ep_copyright_add_num_12_m(self, value):
        self._ep_copyright_add_num_12_m = value
    @property
    def ep_copyright_total_num(self):
        return self._ep_copyright_total_num

    @ep_copyright_total_num.setter
    def ep_copyright_total_num(self, value):
        self._ep_copyright_total_num = value
    @property
    def ep_corrupt_brib_legal_case_num_12_m(self):
        return self._ep_corrupt_brib_legal_case_num_12_m

    @ep_corrupt_brib_legal_case_num_12_m.setter
    def ep_corrupt_brib_legal_case_num_12_m(self, value):
        self._ep_corrupt_brib_legal_case_num_12_m = value
    @property
    def ep_criminal_case_num_12_m(self):
        return self._ep_criminal_case_num_12_m

    @ep_criminal_case_num_12_m.setter
    def ep_criminal_case_num_12_m(self, value):
        self._ep_criminal_case_num_12_m = value
    @property
    def ep_down_rating_bond_num_12_m(self):
        return self._ep_down_rating_bond_num_12_m

    @ep_down_rating_bond_num_12_m.setter
    def ep_down_rating_bond_num_12_m(self, value):
        self._ep_down_rating_bond_num_12_m = value
    @property
    def ep_down_rating_issuer_num_12_m(self):
        return self._ep_down_rating_issuer_num_12_m

    @ep_down_rating_issuer_num_12_m.setter
    def ep_down_rating_issuer_num_12_m(self, value):
        self._ep_down_rating_issuer_num_12_m = value
    @property
    def ep_energy_consume_per_rvn(self):
        return self._ep_energy_consume_per_rvn

    @ep_energy_consume_per_rvn.setter
    def ep_energy_consume_per_rvn(self, value):
        self._ep_energy_consume_per_rvn = value
    @property
    def ep_env_evaluate_12_m(self):
        return self._ep_env_evaluate_12_m

    @ep_env_evaluate_12_m.setter
    def ep_env_evaluate_12_m(self, value):
        self._ep_env_evaluate_12_m = value
    @property
    def ep_env_evaluate_adj_12_m(self):
        return self._ep_env_evaluate_adj_12_m

    @ep_env_evaluate_adj_12_m.setter
    def ep_env_evaluate_adj_12_m(self, value):
        self._ep_env_evaluate_adj_12_m = value
    @property
    def ep_env_legal_case_num_12_m(self):
        return self._ep_env_legal_case_num_12_m

    @ep_env_legal_case_num_12_m.setter
    def ep_env_legal_case_num_12_m(self, value):
        self._ep_env_legal_case_num_12_m = value
    @property
    def ep_env_penalty_amt_12_m(self):
        return self._ep_env_penalty_amt_12_m

    @ep_env_penalty_amt_12_m.setter
    def ep_env_penalty_amt_12_m(self, value):
        self._ep_env_penalty_amt_12_m = value
    @property
    def ep_env_penalty_num_12_m(self):
        return self._ep_env_penalty_num_12_m

    @ep_env_penalty_num_12_m.setter
    def ep_env_penalty_num_12_m(self, value):
        self._ep_env_penalty_num_12_m = value
    @property
    def ep_env_penalty_top_type_12_m(self):
        return self._ep_env_penalty_top_type_12_m

    @ep_env_penalty_top_type_12_m.setter
    def ep_env_penalty_top_type_12_m(self, value):
        self._ep_env_penalty_top_type_12_m = value
    @property
    def ep_fake_prop_penalty_num_12_m(self):
        return self._ep_fake_prop_penalty_num_12_m

    @ep_fake_prop_penalty_num_12_m.setter
    def ep_fake_prop_penalty_num_12_m(self, value):
        self._ep_fake_prop_penalty_num_12_m = value
    @property
    def ep_fd(self):
        return self._ep_fd

    @ep_fd.setter
    def ep_fd(self, value):
        self._ep_fd = value
    @property
    def ep_fire_penalty_amt_12_m(self):
        return self._ep_fire_penalty_amt_12_m

    @ep_fire_penalty_amt_12_m.setter
    def ep_fire_penalty_amt_12_m(self, value):
        self._ep_fire_penalty_amt_12_m = value
    @property
    def ep_fire_penalty_num_12_m(self):
        return self._ep_fire_penalty_num_12_m

    @ep_fire_penalty_num_12_m.setter
    def ep_fire_penalty_num_12_m(self, value):
        self._ep_fire_penalty_num_12_m = value
    @property
    def ep_fire_penalty_top_type_12_m(self):
        return self._ep_fire_penalty_top_type_12_m

    @ep_fire_penalty_top_type_12_m.setter
    def ep_fire_penalty_top_type_12_m(self, value):
        self._ep_fire_penalty_top_type_12_m = value
    @property
    def ep_force_excute_num_12_m(self):
        return self._ep_force_excute_num_12_m

    @ep_force_excute_num_12_m.setter
    def ep_force_excute_num_12_m(self, value):
        self._ep_force_excute_num_12_m = value
    @property
    def ep_founding_years(self):
        return self._ep_founding_years

    @ep_founding_years.setter
    def ep_founding_years(self, value):
        self._ep_founding_years = value
    @property
    def ep_group(self):
        return self._ep_group

    @ep_group.setter
    def ep_group(self, value):
        self._ep_group = value
    @property
    def ep_holder_eqty_frez_amt_12_m(self):
        return self._ep_holder_eqty_frez_amt_12_m

    @ep_holder_eqty_frez_amt_12_m.setter
    def ep_holder_eqty_frez_amt_12_m(self, value):
        self._ep_holder_eqty_frez_amt_12_m = value
    @property
    def ep_holder_eqty_frez_num_12_m(self):
        return self._ep_holder_eqty_frez_num_12_m

    @ep_holder_eqty_frez_num_12_m.setter
    def ep_holder_eqty_frez_num_12_m(self, value):
        self._ep_holder_eqty_frez_num_12_m = value
    @property
    def ep_holder_eqty_frez_ratio_12_m(self):
        return self._ep_holder_eqty_frez_ratio_12_m

    @ep_holder_eqty_frez_ratio_12_m.setter
    def ep_holder_eqty_frez_ratio_12_m(self, value):
        self._ep_holder_eqty_frez_ratio_12_m = value
    @property
    def ep_holder_eqty_frez_ratio_12_m_new(self):
        return self._ep_holder_eqty_frez_ratio_12_m_new

    @ep_holder_eqty_frez_ratio_12_m_new.setter
    def ep_holder_eqty_frez_ratio_12_m_new(self, value):
        self._ep_holder_eqty_frez_ratio_12_m_new = value
    @property
    def ep_holder_eqty_pledge_amt_12_m(self):
        return self._ep_holder_eqty_pledge_amt_12_m

    @ep_holder_eqty_pledge_amt_12_m.setter
    def ep_holder_eqty_pledge_amt_12_m(self, value):
        self._ep_holder_eqty_pledge_amt_12_m = value
    @property
    def ep_holder_eqty_pledge_num_12_m(self):
        return self._ep_holder_eqty_pledge_num_12_m

    @ep_holder_eqty_pledge_num_12_m.setter
    def ep_holder_eqty_pledge_num_12_m(self, value):
        self._ep_holder_eqty_pledge_num_12_m = value
    @property
    def ep_holder_eqty_pledge_ratio_12_m(self):
        return self._ep_holder_eqty_pledge_ratio_12_m

    @ep_holder_eqty_pledge_ratio_12_m.setter
    def ep_holder_eqty_pledge_ratio_12_m(self, value):
        self._ep_holder_eqty_pledge_ratio_12_m = value
    @property
    def ep_hr_legal_case_num_12_m(self):
        return self._ep_hr_legal_case_num_12_m

    @ep_hr_legal_case_num_12_m.setter
    def ep_hr_legal_case_num_12_m(self, value):
        self._ep_hr_legal_case_num_12_m = value
    @property
    def ep_hr_penalty_amt_12_m(self):
        return self._ep_hr_penalty_amt_12_m

    @ep_hr_penalty_amt_12_m.setter
    def ep_hr_penalty_amt_12_m(self, value):
        self._ep_hr_penalty_amt_12_m = value
    @property
    def ep_hr_penalty_num_12_m(self):
        return self._ep_hr_penalty_num_12_m

    @ep_hr_penalty_num_12_m.setter
    def ep_hr_penalty_num_12_m(self, value):
        self._ep_hr_penalty_num_12_m = value
    @property
    def ep_hr_penalty_top_type_12_m(self):
        return self._ep_hr_penalty_top_type_12_m

    @ep_hr_penalty_top_type_12_m.setter
    def ep_hr_penalty_top_type_12_m(self, value):
        self._ep_hr_penalty_top_type_12_m = value
    @property
    def ep_hzd_penalty_num_12_m(self):
        return self._ep_hzd_penalty_num_12_m

    @ep_hzd_penalty_num_12_m.setter
    def ep_hzd_penalty_num_12_m(self, value):
        self._ep_hzd_penalty_num_12_m = value
    @property
    def ep_hzd_penalty_top_type_12_m(self):
        return self._ep_hzd_penalty_top_type_12_m

    @ep_hzd_penalty_top_type_12_m.setter
    def ep_hzd_penalty_top_type_12_m(self, value):
        self._ep_hzd_penalty_top_type_12_m = value
    @property
    def ep_icp_add_num_12_m(self):
        return self._ep_icp_add_num_12_m

    @ep_icp_add_num_12_m.setter
    def ep_icp_add_num_12_m(self, value):
        self._ep_icp_add_num_12_m = value
    @property
    def ep_industry_lv_1_code(self):
        return self._ep_industry_lv_1_code

    @ep_industry_lv_1_code.setter
    def ep_industry_lv_1_code(self, value):
        self._ep_industry_lv_1_code = value
    @property
    def ep_industry_lv_2_code(self):
        return self._ep_industry_lv_2_code

    @ep_industry_lv_2_code.setter
    def ep_industry_lv_2_code(self, value):
        self._ep_industry_lv_2_code = value
    @property
    def ep_industry_lv_3_code(self):
        return self._ep_industry_lv_3_code

    @ep_industry_lv_3_code.setter
    def ep_industry_lv_3_code(self, value):
        self._ep_industry_lv_3_code = value
    @property
    def ep_industry_lv_4_code(self):
        return self._ep_industry_lv_4_code

    @ep_industry_lv_4_code.setter
    def ep_industry_lv_4_code(self, value):
        self._ep_industry_lv_4_code = value
    @property
    def ep_investor_eqty_adj_num_12_m(self):
        return self._ep_investor_eqty_adj_num_12_m

    @ep_investor_eqty_adj_num_12_m.setter
    def ep_investor_eqty_adj_num_12_m(self, value):
        self._ep_investor_eqty_adj_num_12_m = value
    @property
    def ep_ip_legal_case_num_12_m(self):
        return self._ep_ip_legal_case_num_12_m

    @ep_ip_legal_case_num_12_m.setter
    def ep_ip_legal_case_num_12_m(self, value):
        self._ep_ip_legal_case_num_12_m = value
    @property
    def ep_lastyear_ann_rpt_disclose_flag(self):
        return self._ep_lastyear_ann_rpt_disclose_flag

    @ep_lastyear_ann_rpt_disclose_flag.setter
    def ep_lastyear_ann_rpt_disclose_flag(self, value):
        self._ep_lastyear_ann_rpt_disclose_flag = value
    @property
    def ep_latest_ann_rpt_audit_flag(self):
        return self._ep_latest_ann_rpt_audit_flag

    @ep_latest_ann_rpt_audit_flag.setter
    def ep_latest_ann_rpt_audit_flag(self, value):
        self._ep_latest_ann_rpt_audit_flag = value
    @property
    def ep_latest_ann_rpt_audit_opinion(self):
        return self._ep_latest_ann_rpt_audit_opinion

    @ep_latest_ann_rpt_audit_opinion.setter
    def ep_latest_ann_rpt_audit_opinion(self, value):
        self._ep_latest_ann_rpt_audit_opinion = value
    @property
    def ep_legal_person_adj_num_12_m(self):
        return self._ep_legal_person_adj_num_12_m

    @ep_legal_person_adj_num_12_m.setter
    def ep_legal_person_adj_num_12_m(self, value):
        self._ep_legal_person_adj_num_12_m = value
    @property
    def ep_lost_credit_excute_num_12_m(self):
        return self._ep_lost_credit_excute_num_12_m

    @ep_lost_credit_excute_num_12_m.setter
    def ep_lost_credit_excute_num_12_m(self, value):
        self._ep_lost_credit_excute_num_12_m = value
    @property
    def ep_lost_credit_hist_num_12_m(self):
        return self._ep_lost_credit_hist_num_12_m

    @ep_lost_credit_hist_num_12_m.setter
    def ep_lost_credit_hist_num_12_m(self, value):
        self._ep_lost_credit_hist_num_12_m = value
    @property
    def ep_mom_risk_12_m_flag(self):
        return self._ep_mom_risk_12_m_flag

    @ep_mom_risk_12_m_flag.setter
    def ep_mom_risk_12_m_flag(self, value):
        self._ep_mom_risk_12_m_flag = value
    @property
    def ep_name(self):
        return self._ep_name

    @ep_name.setter
    def ep_name(self, value):
        self._ep_name = value
    @property
    def ep_nephew_risk_12_m_flag(self):
        return self._ep_nephew_risk_12_m_flag

    @ep_nephew_risk_12_m_flag.setter
    def ep_nephew_risk_12_m_flag(self, value):
        self._ep_nephew_risk_12_m_flag = value
    @property
    def ep_oprt_scope(self):
        return self._ep_oprt_scope

    @ep_oprt_scope.setter
    def ep_oprt_scope(self, value):
        self._ep_oprt_scope = value
    @property
    def ep_org_reg_cptl(self):
        return self._ep_org_reg_cptl

    @ep_org_reg_cptl.setter
    def ep_org_reg_cptl(self, value):
        self._ep_org_reg_cptl = value
    @property
    def ep_org_reg_cptl_curcy(self):
        return self._ep_org_reg_cptl_curcy

    @ep_org_reg_cptl_curcy.setter
    def ep_org_reg_cptl_curcy(self, value):
        self._ep_org_reg_cptl_curcy = value
    @property
    def ep_org_reg_time(self):
        return self._ep_org_reg_time

    @ep_org_reg_time.setter
    def ep_org_reg_time(self, value):
        self._ep_org_reg_time = value
    @property
    def ep_org_status(self):
        return self._ep_org_status

    @ep_org_status.setter
    def ep_org_status(self, value):
        self._ep_org_status = value
    @property
    def ep_other_legal_case_num_12_m(self):
        return self._ep_other_legal_case_num_12_m

    @ep_other_legal_case_num_12_m.setter
    def ep_other_legal_case_num_12_m(self, value):
        self._ep_other_legal_case_num_12_m = value
    @property
    def ep_other_penalty_amt_12_m(self):
        return self._ep_other_penalty_amt_12_m

    @ep_other_penalty_amt_12_m.setter
    def ep_other_penalty_amt_12_m(self, value):
        self._ep_other_penalty_amt_12_m = value
    @property
    def ep_other_penalty_num_12_m(self):
        return self._ep_other_penalty_num_12_m

    @ep_other_penalty_num_12_m.setter
    def ep_other_penalty_num_12_m(self, value):
        self._ep_other_penalty_num_12_m = value
    @property
    def ep_other_penalty_top_type_12_m(self):
        return self._ep_other_penalty_top_type_12_m

    @ep_other_penalty_top_type_12_m.setter
    def ep_other_penalty_top_type_12_m(self, value):
        self._ep_other_penalty_top_type_12_m = value
    @property
    def ep_patent_add_num_12_m(self):
        return self._ep_patent_add_num_12_m

    @ep_patent_add_num_12_m.setter
    def ep_patent_add_num_12_m(self, value):
        self._ep_patent_add_num_12_m = value
    @property
    def ep_patent_total_num(self):
        return self._ep_patent_total_num

    @ep_patent_total_num.setter
    def ep_patent_total_num(self, value):
        self._ep_patent_total_num = value
    @property
    def ep_private_lend_legal_case_num_12_m(self):
        return self._ep_private_lend_legal_case_num_12_m

    @ep_private_lend_legal_case_num_12_m.setter
    def ep_private_lend_legal_case_num_12_m(self, value):
        self._ep_private_lend_legal_case_num_12_m = value
    @property
    def ep_qlty_penalty_amt_12_m(self):
        return self._ep_qlty_penalty_amt_12_m

    @ep_qlty_penalty_amt_12_m.setter
    def ep_qlty_penalty_amt_12_m(self, value):
        self._ep_qlty_penalty_amt_12_m = value
    @property
    def ep_qlty_penalty_num_12_m(self):
        return self._ep_qlty_penalty_num_12_m

    @ep_qlty_penalty_num_12_m.setter
    def ep_qlty_penalty_num_12_m(self, value):
        self._ep_qlty_penalty_num_12_m = value
    @property
    def ep_qlty_penalty_top_type_12_m(self):
        return self._ep_qlty_penalty_top_type_12_m

    @ep_qlty_penalty_top_type_12_m.setter
    def ep_qlty_penalty_top_type_12_m(self, value):
        self._ep_qlty_penalty_top_type_12_m = value
    @property
    def ep_reg_addr(self):
        return self._ep_reg_addr

    @ep_reg_addr.setter
    def ep_reg_addr(self, value):
        self._ep_reg_addr = value
    @property
    def ep_reg_cptl_adj_ratio_12_m(self):
        return self._ep_reg_cptl_adj_ratio_12_m

    @ep_reg_cptl_adj_ratio_12_m.setter
    def ep_reg_cptl_adj_ratio_12_m(self, value):
        self._ep_reg_cptl_adj_ratio_12_m = value
    @property
    def ep_resource_other_dependence(self):
        return self._ep_resource_other_dependence

    @ep_resource_other_dependence.setter
    def ep_resource_other_dependence(self, value):
        self._ep_resource_other_dependence = value
    @property
    def ep_resource_water_dependence(self):
        return self._ep_resource_water_dependence

    @ep_resource_water_dependence.setter
    def ep_resource_water_dependence(self, value):
        self._ep_resource_water_dependence = value
    @property
    def ep_root_risk_12_m_flag(self):
        return self._ep_root_risk_12_m_flag

    @ep_root_risk_12_m_flag.setter
    def ep_root_risk_12_m_flag(self, value):
        self._ep_root_risk_12_m_flag = value
    @property
    def ep_secu_penalty_amt_12_m(self):
        return self._ep_secu_penalty_amt_12_m

    @ep_secu_penalty_amt_12_m.setter
    def ep_secu_penalty_amt_12_m(self, value):
        self._ep_secu_penalty_amt_12_m = value
    @property
    def ep_secu_penalty_num_12_m(self):
        return self._ep_secu_penalty_num_12_m

    @ep_secu_penalty_num_12_m.setter
    def ep_secu_penalty_num_12_m(self, value):
        self._ep_secu_penalty_num_12_m = value
    @property
    def ep_secu_penalty_top_type_12_m(self):
        return self._ep_secu_penalty_top_type_12_m

    @ep_secu_penalty_top_type_12_m.setter
    def ep_secu_penalty_top_type_12_m(self, value):
        self._ep_secu_penalty_top_type_12_m = value
    @property
    def ep_serious_illegal_list_flag(self):
        return self._ep_serious_illegal_list_flag

    @ep_serious_illegal_list_flag.setter
    def ep_serious_illegal_list_flag(self, value):
        self._ep_serious_illegal_list_flag = value
    @property
    def ep_sibling_risk_12_m_flag(self):
        return self._ep_sibling_risk_12_m_flag

    @ep_sibling_risk_12_m_flag.setter
    def ep_sibling_risk_12_m_flag(self, value):
        self._ep_sibling_risk_12_m_flag = value
    @property
    def ep_solid_emi_per_rvn(self):
        return self._ep_solid_emi_per_rvn

    @ep_solid_emi_per_rvn.setter
    def ep_solid_emi_per_rvn(self, value):
        self._ep_solid_emi_per_rvn = value
    @property
    def ep_staff_num_adj_rate_12_m(self):
        return self._ep_staff_num_adj_rate_12_m

    @ep_staff_num_adj_rate_12_m.setter
    def ep_staff_num_adj_rate_12_m(self, value):
        self._ep_staff_num_adj_rate_12_m = value
    @property
    def ep_status(self):
        return self._ep_status

    @ep_status.setter
    def ep_status(self, value):
        self._ep_status = value
    @property
    def ep_tax_abnor_acct_num_12_m(self):
        return self._ep_tax_abnor_acct_num_12_m

    @ep_tax_abnor_acct_num_12_m.setter
    def ep_tax_abnor_acct_num_12_m(self, value):
        self._ep_tax_abnor_acct_num_12_m = value
    @property
    def ep_tax_credit_adj_dic_latest(self):
        return self._ep_tax_credit_adj_dic_latest

    @ep_tax_credit_adj_dic_latest.setter
    def ep_tax_credit_adj_dic_latest(self, value):
        self._ep_tax_credit_adj_dic_latest = value
    @property
    def ep_tax_penalty_amt_12_m(self):
        return self._ep_tax_penalty_amt_12_m

    @ep_tax_penalty_amt_12_m.setter
    def ep_tax_penalty_amt_12_m(self, value):
        self._ep_tax_penalty_amt_12_m = value
    @property
    def ep_tax_penalty_num_12_m(self):
        return self._ep_tax_penalty_num_12_m

    @ep_tax_penalty_num_12_m.setter
    def ep_tax_penalty_num_12_m(self, value):
        self._ep_tax_penalty_num_12_m = value
    @property
    def ep_tax_penalty_top_type_12_m(self):
        return self._ep_tax_penalty_top_type_12_m

    @ep_tax_penalty_top_type_12_m.setter
    def ep_tax_penalty_top_type_12_m(self, value):
        self._ep_tax_penalty_top_type_12_m = value
    @property
    def ep_uncle_risk_12_m_flag(self):
        return self._ep_uncle_risk_12_m_flag

    @ep_uncle_risk_12_m_flag.setter
    def ep_uncle_risk_12_m_flag(self, value):
        self._ep_uncle_risk_12_m_flag = value
    @property
    def ep_unfair_compt_legal_case_num_12_m(self):
        return self._ep_unfair_compt_legal_case_num_12_m

    @ep_unfair_compt_legal_case_num_12_m.setter
    def ep_unfair_compt_legal_case_num_12_m(self, value):
        self._ep_unfair_compt_legal_case_num_12_m = value
    @property
    def evaluate_time(self):
        return self._evaluate_time

    @evaluate_time.setter
    def evaluate_time(self, value):
        self._evaluate_time = value
    @property
    def excu_limi_high_consum_12_m_flag(self):
        return self._excu_limi_high_consum_12_m_flag

    @excu_limi_high_consum_12_m_flag.setter
    def excu_limi_high_consum_12_m_flag(self, value):
        self._excu_limi_high_consum_12_m_flag = value
    @property
    def issue_green_bond_flag(self):
        return self._issue_green_bond_flag

    @issue_green_bond_flag.setter
    def issue_green_bond_flag(self, value):
        self._issue_green_bond_flag = value
    @property
    def over_std_gas_emi_last_year_flag(self):
        return self._over_std_gas_emi_last_year_flag

    @over_std_gas_emi_last_year_flag.setter
    def over_std_gas_emi_last_year_flag(self, value):
        self._over_std_gas_emi_last_year_flag = value
    @property
    def over_std_water_emi_last_year_flag(self):
        return self._over_std_water_emi_last_year_flag

    @over_std_water_emi_last_year_flag.setter
    def over_std_water_emi_last_year_flag(self, value):
        self._over_std_water_emi_last_year_flag = value
    @property
    def over_vol_gas_emi_last_year_flag(self):
        return self._over_vol_gas_emi_last_year_flag

    @over_vol_gas_emi_last_year_flag.setter
    def over_vol_gas_emi_last_year_flag(self, value):
        self._over_vol_gas_emi_last_year_flag = value
    @property
    def over_vol_water_emi_last_year_flag(self):
        return self._over_vol_water_emi_last_year_flag

    @over_vol_water_emi_last_year_flag.setter
    def over_vol_water_emi_last_year_flag(self, value):
        self._over_vol_water_emi_last_year_flag = value
    @property
    def owing_tax_12_m_flag(self):
        return self._owing_tax_12_m_flag

    @owing_tax_12_m_flag.setter
    def owing_tax_12_m_flag(self, value):
        self._owing_tax_12_m_flag = value
    @property
    def req_emi_adj_12_m_flag(self):
        return self._req_emi_adj_12_m_flag

    @req_emi_adj_12_m_flag.setter
    def req_emi_adj_12_m_flag(self, value):
        self._req_emi_adj_12_m_flag = value
    @property
    def tax_as_pay_12_m_flag(self):
        return self._tax_as_pay_12_m_flag

    @tax_as_pay_12_m_flag.setter
    def tax_as_pay_12_m_flag(self, value):
        self._tax_as_pay_12_m_flag = value
    @property
    def tax_credit_a_level_latest_flag(self):
        return self._tax_credit_a_level_latest_flag

    @tax_credit_a_level_latest_flag.setter
    def tax_credit_a_level_latest_flag(self, value):
        self._tax_credit_a_level_latest_flag = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpEsgInfoQueryResponse, self).parse_response_content(response_content)
        if 'bankrupt_liquid_12_m_flag' in response:
            self.bankrupt_liquid_12_m_flag = response['bankrupt_liquid_12_m_flag']
        if 'emi_licen_ban_num_12_m_flag' in response:
            self.emi_licen_ban_num_12_m_flag = response['emi_licen_ban_num_12_m_flag']
        if 'ep_abn_status_flag' in response:
            self.ep_abn_status_flag = response['ep_abn_status_flag']
        if 'ep_adm_team_adj_num_12_m' in response:
            self.ep_adm_team_adj_num_12_m = response['ep_adm_team_adj_num_12_m']
        if 'ep_big_tax_illegal_num_12_m' in response:
            self.ep_big_tax_illegal_num_12_m = response['ep_big_tax_illegal_num_12_m']
        if 'ep_biggest_share_holder_ratio' in response:
            self.ep_biggest_share_holder_ratio = response['ep_biggest_share_holder_ratio']
        if 'ep_bond_default_flag' in response:
            self.ep_bond_default_flag = response['ep_bond_default_flag']
        if 'ep_bond_defaults_num_12_m' in response:
            self.ep_bond_defaults_num_12_m = response['ep_bond_defaults_num_12_m']
        if 'ep_brand_add_num_12_m' in response:
            self.ep_brand_add_num_12_m = response['ep_brand_add_num_12_m']
        if 'ep_busi_abnor_num_12_m' in response:
            self.ep_busi_abnor_num_12_m = response['ep_busi_abnor_num_12_m']
        if 'ep_busi_abnor_top_type_12_m' in response:
            self.ep_busi_abnor_top_type_12_m = response['ep_busi_abnor_top_type_12_m']
        if 'ep_busi_scope_adj_num_12_m' in response:
            self.ep_busi_scope_adj_num_12_m = response['ep_busi_scope_adj_num_12_m']
        if 'ep_cert_no' in response:
            self.ep_cert_no = response['ep_cert_no']
        if 'ep_cetificate_list' in response:
            self.ep_cetificate_list = response['ep_cetificate_list']
        if 'ep_child_risk_12_m_flag' in response:
            self.ep_child_risk_12_m_flag = response['ep_child_risk_12_m_flag']
        if 'ep_climate_risk_exp' in response:
            self.ep_climate_risk_exp = response['ep_climate_risk_exp']
        if 'ep_co_2_emi_per_rvn' in response:
            self.ep_co_2_emi_per_rvn = response['ep_co_2_emi_per_rvn']
        if 'ep_copyright_add_num_12_m' in response:
            self.ep_copyright_add_num_12_m = response['ep_copyright_add_num_12_m']
        if 'ep_copyright_total_num' in response:
            self.ep_copyright_total_num = response['ep_copyright_total_num']
        if 'ep_corrupt_brib_legal_case_num_12_m' in response:
            self.ep_corrupt_brib_legal_case_num_12_m = response['ep_corrupt_brib_legal_case_num_12_m']
        if 'ep_criminal_case_num_12_m' in response:
            self.ep_criminal_case_num_12_m = response['ep_criminal_case_num_12_m']
        if 'ep_down_rating_bond_num_12_m' in response:
            self.ep_down_rating_bond_num_12_m = response['ep_down_rating_bond_num_12_m']
        if 'ep_down_rating_issuer_num_12_m' in response:
            self.ep_down_rating_issuer_num_12_m = response['ep_down_rating_issuer_num_12_m']
        if 'ep_energy_consume_per_rvn' in response:
            self.ep_energy_consume_per_rvn = response['ep_energy_consume_per_rvn']
        if 'ep_env_evaluate_12_m' in response:
            self.ep_env_evaluate_12_m = response['ep_env_evaluate_12_m']
        if 'ep_env_evaluate_adj_12_m' in response:
            self.ep_env_evaluate_adj_12_m = response['ep_env_evaluate_adj_12_m']
        if 'ep_env_legal_case_num_12_m' in response:
            self.ep_env_legal_case_num_12_m = response['ep_env_legal_case_num_12_m']
        if 'ep_env_penalty_amt_12_m' in response:
            self.ep_env_penalty_amt_12_m = response['ep_env_penalty_amt_12_m']
        if 'ep_env_penalty_num_12_m' in response:
            self.ep_env_penalty_num_12_m = response['ep_env_penalty_num_12_m']
        if 'ep_env_penalty_top_type_12_m' in response:
            self.ep_env_penalty_top_type_12_m = response['ep_env_penalty_top_type_12_m']
        if 'ep_fake_prop_penalty_num_12_m' in response:
            self.ep_fake_prop_penalty_num_12_m = response['ep_fake_prop_penalty_num_12_m']
        if 'ep_fd' in response:
            self.ep_fd = response['ep_fd']
        if 'ep_fire_penalty_amt_12_m' in response:
            self.ep_fire_penalty_amt_12_m = response['ep_fire_penalty_amt_12_m']
        if 'ep_fire_penalty_num_12_m' in response:
            self.ep_fire_penalty_num_12_m = response['ep_fire_penalty_num_12_m']
        if 'ep_fire_penalty_top_type_12_m' in response:
            self.ep_fire_penalty_top_type_12_m = response['ep_fire_penalty_top_type_12_m']
        if 'ep_force_excute_num_12_m' in response:
            self.ep_force_excute_num_12_m = response['ep_force_excute_num_12_m']
        if 'ep_founding_years' in response:
            self.ep_founding_years = response['ep_founding_years']
        if 'ep_group' in response:
            self.ep_group = response['ep_group']
        if 'ep_holder_eqty_frez_amt_12_m' in response:
            self.ep_holder_eqty_frez_amt_12_m = response['ep_holder_eqty_frez_amt_12_m']
        if 'ep_holder_eqty_frez_num_12_m' in response:
            self.ep_holder_eqty_frez_num_12_m = response['ep_holder_eqty_frez_num_12_m']
        if 'ep_holder_eqty_frez_ratio_12_m' in response:
            self.ep_holder_eqty_frez_ratio_12_m = response['ep_holder_eqty_frez_ratio_12_m']
        if 'ep_holder_eqty_frez_ratio_12_m_new' in response:
            self.ep_holder_eqty_frez_ratio_12_m_new = response['ep_holder_eqty_frez_ratio_12_m_new']
        if 'ep_holder_eqty_pledge_amt_12_m' in response:
            self.ep_holder_eqty_pledge_amt_12_m = response['ep_holder_eqty_pledge_amt_12_m']
        if 'ep_holder_eqty_pledge_num_12_m' in response:
            self.ep_holder_eqty_pledge_num_12_m = response['ep_holder_eqty_pledge_num_12_m']
        if 'ep_holder_eqty_pledge_ratio_12_m' in response:
            self.ep_holder_eqty_pledge_ratio_12_m = response['ep_holder_eqty_pledge_ratio_12_m']
        if 'ep_hr_legal_case_num_12_m' in response:
            self.ep_hr_legal_case_num_12_m = response['ep_hr_legal_case_num_12_m']
        if 'ep_hr_penalty_amt_12_m' in response:
            self.ep_hr_penalty_amt_12_m = response['ep_hr_penalty_amt_12_m']
        if 'ep_hr_penalty_num_12_m' in response:
            self.ep_hr_penalty_num_12_m = response['ep_hr_penalty_num_12_m']
        if 'ep_hr_penalty_top_type_12_m' in response:
            self.ep_hr_penalty_top_type_12_m = response['ep_hr_penalty_top_type_12_m']
        if 'ep_hzd_penalty_num_12_m' in response:
            self.ep_hzd_penalty_num_12_m = response['ep_hzd_penalty_num_12_m']
        if 'ep_hzd_penalty_top_type_12_m' in response:
            self.ep_hzd_penalty_top_type_12_m = response['ep_hzd_penalty_top_type_12_m']
        if 'ep_icp_add_num_12_m' in response:
            self.ep_icp_add_num_12_m = response['ep_icp_add_num_12_m']
        if 'ep_industry_lv_1_code' in response:
            self.ep_industry_lv_1_code = response['ep_industry_lv_1_code']
        if 'ep_industry_lv_2_code' in response:
            self.ep_industry_lv_2_code = response['ep_industry_lv_2_code']
        if 'ep_industry_lv_3_code' in response:
            self.ep_industry_lv_3_code = response['ep_industry_lv_3_code']
        if 'ep_industry_lv_4_code' in response:
            self.ep_industry_lv_4_code = response['ep_industry_lv_4_code']
        if 'ep_investor_eqty_adj_num_12_m' in response:
            self.ep_investor_eqty_adj_num_12_m = response['ep_investor_eqty_adj_num_12_m']
        if 'ep_ip_legal_case_num_12_m' in response:
            self.ep_ip_legal_case_num_12_m = response['ep_ip_legal_case_num_12_m']
        if 'ep_lastyear_ann_rpt_disclose_flag' in response:
            self.ep_lastyear_ann_rpt_disclose_flag = response['ep_lastyear_ann_rpt_disclose_flag']
        if 'ep_latest_ann_rpt_audit_flag' in response:
            self.ep_latest_ann_rpt_audit_flag = response['ep_latest_ann_rpt_audit_flag']
        if 'ep_latest_ann_rpt_audit_opinion' in response:
            self.ep_latest_ann_rpt_audit_opinion = response['ep_latest_ann_rpt_audit_opinion']
        if 'ep_legal_person_adj_num_12_m' in response:
            self.ep_legal_person_adj_num_12_m = response['ep_legal_person_adj_num_12_m']
        if 'ep_lost_credit_excute_num_12_m' in response:
            self.ep_lost_credit_excute_num_12_m = response['ep_lost_credit_excute_num_12_m']
        if 'ep_lost_credit_hist_num_12_m' in response:
            self.ep_lost_credit_hist_num_12_m = response['ep_lost_credit_hist_num_12_m']
        if 'ep_mom_risk_12_m_flag' in response:
            self.ep_mom_risk_12_m_flag = response['ep_mom_risk_12_m_flag']
        if 'ep_name' in response:
            self.ep_name = response['ep_name']
        if 'ep_nephew_risk_12_m_flag' in response:
            self.ep_nephew_risk_12_m_flag = response['ep_nephew_risk_12_m_flag']
        if 'ep_oprt_scope' in response:
            self.ep_oprt_scope = response['ep_oprt_scope']
        if 'ep_org_reg_cptl' in response:
            self.ep_org_reg_cptl = response['ep_org_reg_cptl']
        if 'ep_org_reg_cptl_curcy' in response:
            self.ep_org_reg_cptl_curcy = response['ep_org_reg_cptl_curcy']
        if 'ep_org_reg_time' in response:
            self.ep_org_reg_time = response['ep_org_reg_time']
        if 'ep_org_status' in response:
            self.ep_org_status = response['ep_org_status']
        if 'ep_other_legal_case_num_12_m' in response:
            self.ep_other_legal_case_num_12_m = response['ep_other_legal_case_num_12_m']
        if 'ep_other_penalty_amt_12_m' in response:
            self.ep_other_penalty_amt_12_m = response['ep_other_penalty_amt_12_m']
        if 'ep_other_penalty_num_12_m' in response:
            self.ep_other_penalty_num_12_m = response['ep_other_penalty_num_12_m']
        if 'ep_other_penalty_top_type_12_m' in response:
            self.ep_other_penalty_top_type_12_m = response['ep_other_penalty_top_type_12_m']
        if 'ep_patent_add_num_12_m' in response:
            self.ep_patent_add_num_12_m = response['ep_patent_add_num_12_m']
        if 'ep_patent_total_num' in response:
            self.ep_patent_total_num = response['ep_patent_total_num']
        if 'ep_private_lend_legal_case_num_12_m' in response:
            self.ep_private_lend_legal_case_num_12_m = response['ep_private_lend_legal_case_num_12_m']
        if 'ep_qlty_penalty_amt_12_m' in response:
            self.ep_qlty_penalty_amt_12_m = response['ep_qlty_penalty_amt_12_m']
        if 'ep_qlty_penalty_num_12_m' in response:
            self.ep_qlty_penalty_num_12_m = response['ep_qlty_penalty_num_12_m']
        if 'ep_qlty_penalty_top_type_12_m' in response:
            self.ep_qlty_penalty_top_type_12_m = response['ep_qlty_penalty_top_type_12_m']
        if 'ep_reg_addr' in response:
            self.ep_reg_addr = response['ep_reg_addr']
        if 'ep_reg_cptl_adj_ratio_12_m' in response:
            self.ep_reg_cptl_adj_ratio_12_m = response['ep_reg_cptl_adj_ratio_12_m']
        if 'ep_resource_other_dependence' in response:
            self.ep_resource_other_dependence = response['ep_resource_other_dependence']
        if 'ep_resource_water_dependence' in response:
            self.ep_resource_water_dependence = response['ep_resource_water_dependence']
        if 'ep_root_risk_12_m_flag' in response:
            self.ep_root_risk_12_m_flag = response['ep_root_risk_12_m_flag']
        if 'ep_secu_penalty_amt_12_m' in response:
            self.ep_secu_penalty_amt_12_m = response['ep_secu_penalty_amt_12_m']
        if 'ep_secu_penalty_num_12_m' in response:
            self.ep_secu_penalty_num_12_m = response['ep_secu_penalty_num_12_m']
        if 'ep_secu_penalty_top_type_12_m' in response:
            self.ep_secu_penalty_top_type_12_m = response['ep_secu_penalty_top_type_12_m']
        if 'ep_serious_illegal_list_flag' in response:
            self.ep_serious_illegal_list_flag = response['ep_serious_illegal_list_flag']
        if 'ep_sibling_risk_12_m_flag' in response:
            self.ep_sibling_risk_12_m_flag = response['ep_sibling_risk_12_m_flag']
        if 'ep_solid_emi_per_rvn' in response:
            self.ep_solid_emi_per_rvn = response['ep_solid_emi_per_rvn']
        if 'ep_staff_num_adj_rate_12_m' in response:
            self.ep_staff_num_adj_rate_12_m = response['ep_staff_num_adj_rate_12_m']
        if 'ep_status' in response:
            self.ep_status = response['ep_status']
        if 'ep_tax_abnor_acct_num_12_m' in response:
            self.ep_tax_abnor_acct_num_12_m = response['ep_tax_abnor_acct_num_12_m']
        if 'ep_tax_credit_adj_dic_latest' in response:
            self.ep_tax_credit_adj_dic_latest = response['ep_tax_credit_adj_dic_latest']
        if 'ep_tax_penalty_amt_12_m' in response:
            self.ep_tax_penalty_amt_12_m = response['ep_tax_penalty_amt_12_m']
        if 'ep_tax_penalty_num_12_m' in response:
            self.ep_tax_penalty_num_12_m = response['ep_tax_penalty_num_12_m']
        if 'ep_tax_penalty_top_type_12_m' in response:
            self.ep_tax_penalty_top_type_12_m = response['ep_tax_penalty_top_type_12_m']
        if 'ep_uncle_risk_12_m_flag' in response:
            self.ep_uncle_risk_12_m_flag = response['ep_uncle_risk_12_m_flag']
        if 'ep_unfair_compt_legal_case_num_12_m' in response:
            self.ep_unfair_compt_legal_case_num_12_m = response['ep_unfair_compt_legal_case_num_12_m']
        if 'evaluate_time' in response:
            self.evaluate_time = response['evaluate_time']
        if 'excu_limi_high_consum_12_m_flag' in response:
            self.excu_limi_high_consum_12_m_flag = response['excu_limi_high_consum_12_m_flag']
        if 'issue_green_bond_flag' in response:
            self.issue_green_bond_flag = response['issue_green_bond_flag']
        if 'over_std_gas_emi_last_year_flag' in response:
            self.over_std_gas_emi_last_year_flag = response['over_std_gas_emi_last_year_flag']
        if 'over_std_water_emi_last_year_flag' in response:
            self.over_std_water_emi_last_year_flag = response['over_std_water_emi_last_year_flag']
        if 'over_vol_gas_emi_last_year_flag' in response:
            self.over_vol_gas_emi_last_year_flag = response['over_vol_gas_emi_last_year_flag']
        if 'over_vol_water_emi_last_year_flag' in response:
            self.over_vol_water_emi_last_year_flag = response['over_vol_water_emi_last_year_flag']
        if 'owing_tax_12_m_flag' in response:
            self.owing_tax_12_m_flag = response['owing_tax_12_m_flag']
        if 'req_emi_adj_12_m_flag' in response:
            self.req_emi_adj_12_m_flag = response['req_emi_adj_12_m_flag']
        if 'tax_as_pay_12_m_flag' in response:
            self.tax_as_pay_12_m_flag = response['tax_as_pay_12_m_flag']
        if 'tax_credit_a_level_latest_flag' in response:
            self.tax_credit_a_level_latest_flag = response['tax_credit_a_level_latest_flag']
