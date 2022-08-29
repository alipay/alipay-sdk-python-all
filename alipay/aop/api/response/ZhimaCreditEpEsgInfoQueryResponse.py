#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditEpEsgInfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpEsgInfoQueryResponse, self).__init__()
        self._bankrupt_liquid_12_m_flag = None
        self._emi_licen_ban_num_12_m_flag = None
        self._ep_adm_team_adj_num_12_m = None
        self._ep_big_tax_illegal_num_12_m = None
        self._ep_bond_defaults_num_12_m = None
        self._ep_brand_add_num_12_m = None
        self._ep_busi_abnor_num_12_m = None
        self._ep_busi_abnor_top_type_12_m = None
        self._ep_busi_scope_adj_num_12_m = None
        self._ep_cert_no = None
        self._ep_cetificate_list = None
        self._ep_copyright_add_num_12_m = None
        self._ep_criminal_case_num_12_m = None
        self._ep_down_rating_bond_num_12_m = None
        self._ep_down_rating_issuer_num_12_m = None
        self._ep_env_evaluate_12_m = None
        self._ep_env_evaluate_adj_12_m = None
        self._ep_env_legal_case_num_12_m = None
        self._ep_env_penalty_amt_12_m = None
        self._ep_env_penalty_num_12_m = None
        self._ep_env_penalty_top_type_12_m = None
        self._ep_fire_penalty_amt_12_m = None
        self._ep_fire_penalty_num_12_m = None
        self._ep_fire_penalty_top_type_12_m = None
        self._ep_force_excute_num_12_m = None
        self._ep_founding_years = None
        self._ep_group = None
        self._ep_holder_eqty_frez_amt_12_m = None
        self._ep_holder_eqty_frez_num_12_m = None
        self._ep_holder_eqty_pledge_amt_12_m = None
        self._ep_holder_eqty_pledge_num_12_m = None
        self._ep_hr_legal_case_num_12_m = None
        self._ep_hr_penalty_amt_12_m = None
        self._ep_hr_penalty_num_12_m = None
        self._ep_hr_penalty_top_type_12_m = None
        self._ep_icp_add_num_12_m = None
        self._ep_investor_eqty_adj_num_12_m = None
        self._ep_ip_legal_case_num_12_m = None
        self._ep_legal_person_adj_num_12_m = None
        self._ep_lost_credit_excute_num_12_m = None
        self._ep_lost_credit_hist_num_12_m = None
        self._ep_name = None
        self._ep_other_legal_case_num_12_m = None
        self._ep_other_penalty_amt_12_m = None
        self._ep_other_penalty_num_12_m = None
        self._ep_other_penalty_top_type_12_m = None
        self._ep_patent_add_num_12_m = None
        self._ep_qlty_penalty_amt_12_m = None
        self._ep_qlty_penalty_num_12_m = None
        self._ep_qlty_penalty_top_type_12_m = None
        self._ep_secu_penalty_amt_12_m = None
        self._ep_secu_penalty_num_12_m = None
        self._ep_secu_penalty_top_type_12_m = None
        self._ep_serious_illegal_list_flag = None
        self._ep_staff_num_adj_rate_12_m = None
        self._ep_status = None
        self._ep_tax_abnor_acct_num_12_m = None
        self._ep_tax_credit_adj_dic_latest = None
        self._ep_tax_penalty_amt_12_m = None
        self._ep_tax_penalty_num_12_m = None
        self._ep_tax_penalty_top_type_12_m = None
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
    def ep_copyright_add_num_12_m(self):
        return self._ep_copyright_add_num_12_m

    @ep_copyright_add_num_12_m.setter
    def ep_copyright_add_num_12_m(self, value):
        self._ep_copyright_add_num_12_m = value
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
    def ep_icp_add_num_12_m(self):
        return self._ep_icp_add_num_12_m

    @ep_icp_add_num_12_m.setter
    def ep_icp_add_num_12_m(self, value):
        self._ep_icp_add_num_12_m = value
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
    def ep_name(self):
        return self._ep_name

    @ep_name.setter
    def ep_name(self, value):
        self._ep_name = value
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
        if 'ep_adm_team_adj_num_12_m' in response:
            self.ep_adm_team_adj_num_12_m = response['ep_adm_team_adj_num_12_m']
        if 'ep_big_tax_illegal_num_12_m' in response:
            self.ep_big_tax_illegal_num_12_m = response['ep_big_tax_illegal_num_12_m']
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
        if 'ep_copyright_add_num_12_m' in response:
            self.ep_copyright_add_num_12_m = response['ep_copyright_add_num_12_m']
        if 'ep_criminal_case_num_12_m' in response:
            self.ep_criminal_case_num_12_m = response['ep_criminal_case_num_12_m']
        if 'ep_down_rating_bond_num_12_m' in response:
            self.ep_down_rating_bond_num_12_m = response['ep_down_rating_bond_num_12_m']
        if 'ep_down_rating_issuer_num_12_m' in response:
            self.ep_down_rating_issuer_num_12_m = response['ep_down_rating_issuer_num_12_m']
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
        if 'ep_holder_eqty_pledge_amt_12_m' in response:
            self.ep_holder_eqty_pledge_amt_12_m = response['ep_holder_eqty_pledge_amt_12_m']
        if 'ep_holder_eqty_pledge_num_12_m' in response:
            self.ep_holder_eqty_pledge_num_12_m = response['ep_holder_eqty_pledge_num_12_m']
        if 'ep_hr_legal_case_num_12_m' in response:
            self.ep_hr_legal_case_num_12_m = response['ep_hr_legal_case_num_12_m']
        if 'ep_hr_penalty_amt_12_m' in response:
            self.ep_hr_penalty_amt_12_m = response['ep_hr_penalty_amt_12_m']
        if 'ep_hr_penalty_num_12_m' in response:
            self.ep_hr_penalty_num_12_m = response['ep_hr_penalty_num_12_m']
        if 'ep_hr_penalty_top_type_12_m' in response:
            self.ep_hr_penalty_top_type_12_m = response['ep_hr_penalty_top_type_12_m']
        if 'ep_icp_add_num_12_m' in response:
            self.ep_icp_add_num_12_m = response['ep_icp_add_num_12_m']
        if 'ep_investor_eqty_adj_num_12_m' in response:
            self.ep_investor_eqty_adj_num_12_m = response['ep_investor_eqty_adj_num_12_m']
        if 'ep_ip_legal_case_num_12_m' in response:
            self.ep_ip_legal_case_num_12_m = response['ep_ip_legal_case_num_12_m']
        if 'ep_legal_person_adj_num_12_m' in response:
            self.ep_legal_person_adj_num_12_m = response['ep_legal_person_adj_num_12_m']
        if 'ep_lost_credit_excute_num_12_m' in response:
            self.ep_lost_credit_excute_num_12_m = response['ep_lost_credit_excute_num_12_m']
        if 'ep_lost_credit_hist_num_12_m' in response:
            self.ep_lost_credit_hist_num_12_m = response['ep_lost_credit_hist_num_12_m']
        if 'ep_name' in response:
            self.ep_name = response['ep_name']
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
        if 'ep_qlty_penalty_amt_12_m' in response:
            self.ep_qlty_penalty_amt_12_m = response['ep_qlty_penalty_amt_12_m']
        if 'ep_qlty_penalty_num_12_m' in response:
            self.ep_qlty_penalty_num_12_m = response['ep_qlty_penalty_num_12_m']
        if 'ep_qlty_penalty_top_type_12_m' in response:
            self.ep_qlty_penalty_top_type_12_m = response['ep_qlty_penalty_top_type_12_m']
        if 'ep_secu_penalty_amt_12_m' in response:
            self.ep_secu_penalty_amt_12_m = response['ep_secu_penalty_amt_12_m']
        if 'ep_secu_penalty_num_12_m' in response:
            self.ep_secu_penalty_num_12_m = response['ep_secu_penalty_num_12_m']
        if 'ep_secu_penalty_top_type_12_m' in response:
            self.ep_secu_penalty_top_type_12_m = response['ep_secu_penalty_top_type_12_m']
        if 'ep_serious_illegal_list_flag' in response:
            self.ep_serious_illegal_list_flag = response['ep_serious_illegal_list_flag']
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
