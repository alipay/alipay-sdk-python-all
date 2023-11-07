#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.IssueRuleInfo import IssueRuleInfo
from alipay.aop.api.domain.StandardInfo import StandardInfo
from alipay.aop.api.domain.StandardInfo import StandardInfo


class AlipayEbppInvoiceInstitutionDetailinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInvoiceInstitutionDetailinfoQueryResponse, self).__init__()
        self._adapter_type = None
        self._consult_mode = None
        self._effective = None
        self._effective_end_date = None
        self._effective_start_date = None
        self._expense_type = None
        self._institution_desc = None
        self._institution_id = None
        self._institution_name = None
        self._issue_rule_info_list = None
        self._outer_source_id = None
        self._owner_id_list = None
        self._owner_open_id_list = None
        self._scene_type = None
        self._standard_info_detail_list = None
        self._standard_info_list = None

    @property
    def adapter_type(self):
        return self._adapter_type

    @adapter_type.setter
    def adapter_type(self, value):
        self._adapter_type = value
    @property
    def consult_mode(self):
        return self._consult_mode

    @consult_mode.setter
    def consult_mode(self, value):
        self._consult_mode = value
    @property
    def effective(self):
        return self._effective

    @effective.setter
    def effective(self, value):
        self._effective = value
    @property
    def effective_end_date(self):
        return self._effective_end_date

    @effective_end_date.setter
    def effective_end_date(self, value):
        self._effective_end_date = value
    @property
    def effective_start_date(self):
        return self._effective_start_date

    @effective_start_date.setter
    def effective_start_date(self, value):
        self._effective_start_date = value
    @property
    def expense_type(self):
        return self._expense_type

    @expense_type.setter
    def expense_type(self, value):
        self._expense_type = value
    @property
    def institution_desc(self):
        return self._institution_desc

    @institution_desc.setter
    def institution_desc(self, value):
        self._institution_desc = value
    @property
    def institution_id(self):
        return self._institution_id

    @institution_id.setter
    def institution_id(self, value):
        self._institution_id = value
    @property
    def institution_name(self):
        return self._institution_name

    @institution_name.setter
    def institution_name(self, value):
        self._institution_name = value
    @property
    def issue_rule_info_list(self):
        return self._issue_rule_info_list

    @issue_rule_info_list.setter
    def issue_rule_info_list(self, value):
        if isinstance(value, list):
            self._issue_rule_info_list = list()
            for i in value:
                if isinstance(i, IssueRuleInfo):
                    self._issue_rule_info_list.append(i)
                else:
                    self._issue_rule_info_list.append(IssueRuleInfo.from_alipay_dict(i))
    @property
    def outer_source_id(self):
        return self._outer_source_id

    @outer_source_id.setter
    def outer_source_id(self, value):
        self._outer_source_id = value
    @property
    def owner_id_list(self):
        return self._owner_id_list

    @owner_id_list.setter
    def owner_id_list(self, value):
        if isinstance(value, list):
            self._owner_id_list = list()
            for i in value:
                self._owner_id_list.append(i)
    @property
    def owner_open_id_list(self):
        return self._owner_open_id_list

    @owner_open_id_list.setter
    def owner_open_id_list(self, value):
        if isinstance(value, list):
            self._owner_open_id_list = list()
            for i in value:
                self._owner_open_id_list.append(i)
    @property
    def scene_type(self):
        return self._scene_type

    @scene_type.setter
    def scene_type(self, value):
        self._scene_type = value
    @property
    def standard_info_detail_list(self):
        return self._standard_info_detail_list

    @standard_info_detail_list.setter
    def standard_info_detail_list(self, value):
        if isinstance(value, list):
            self._standard_info_detail_list = list()
            for i in value:
                if isinstance(i, StandardInfo):
                    self._standard_info_detail_list.append(i)
                else:
                    self._standard_info_detail_list.append(StandardInfo.from_alipay_dict(i))
    @property
    def standard_info_list(self):
        return self._standard_info_list

    @standard_info_list.setter
    def standard_info_list(self, value):
        if isinstance(value, StandardInfo):
            self._standard_info_list = value
        else:
            self._standard_info_list = StandardInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInvoiceInstitutionDetailinfoQueryResponse, self).parse_response_content(response_content)
        if 'adapter_type' in response:
            self.adapter_type = response['adapter_type']
        if 'consult_mode' in response:
            self.consult_mode = response['consult_mode']
        if 'effective' in response:
            self.effective = response['effective']
        if 'effective_end_date' in response:
            self.effective_end_date = response['effective_end_date']
        if 'effective_start_date' in response:
            self.effective_start_date = response['effective_start_date']
        if 'expense_type' in response:
            self.expense_type = response['expense_type']
        if 'institution_desc' in response:
            self.institution_desc = response['institution_desc']
        if 'institution_id' in response:
            self.institution_id = response['institution_id']
        if 'institution_name' in response:
            self.institution_name = response['institution_name']
        if 'issue_rule_info_list' in response:
            self.issue_rule_info_list = response['issue_rule_info_list']
        if 'outer_source_id' in response:
            self.outer_source_id = response['outer_source_id']
        if 'owner_id_list' in response:
            self.owner_id_list = response['owner_id_list']
        if 'owner_open_id_list' in response:
            self.owner_open_id_list = response['owner_open_id_list']
        if 'scene_type' in response:
            self.scene_type = response['scene_type']
        if 'standard_info_detail_list' in response:
            self.standard_info_detail_list = response['standard_info_detail_list']
        if 'standard_info_list' in response:
            self.standard_info_list = response['standard_info_list']
