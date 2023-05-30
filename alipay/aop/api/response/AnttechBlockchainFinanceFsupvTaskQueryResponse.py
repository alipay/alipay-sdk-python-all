#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechBlockchainFinanceFsupvTaskQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainFinanceFsupvTaskQueryResponse, self).__init__()
        self._fund_supv_task_id = None
        self._supervised_desensitized_access_no = None
        self._supervised_special_account_no = None
        self._supv_agreement_no = None
        self._supv_end = None
        self._supv_start = None

    @property
    def fund_supv_task_id(self):
        return self._fund_supv_task_id

    @fund_supv_task_id.setter
    def fund_supv_task_id(self, value):
        self._fund_supv_task_id = value
    @property
    def supervised_desensitized_access_no(self):
        return self._supervised_desensitized_access_no

    @supervised_desensitized_access_no.setter
    def supervised_desensitized_access_no(self, value):
        self._supervised_desensitized_access_no = value
    @property
    def supervised_special_account_no(self):
        return self._supervised_special_account_no

    @supervised_special_account_no.setter
    def supervised_special_account_no(self, value):
        self._supervised_special_account_no = value
    @property
    def supv_agreement_no(self):
        return self._supv_agreement_no

    @supv_agreement_no.setter
    def supv_agreement_no(self, value):
        self._supv_agreement_no = value
    @property
    def supv_end(self):
        return self._supv_end

    @supv_end.setter
    def supv_end(self, value):
        self._supv_end = value
    @property
    def supv_start(self):
        return self._supv_start

    @supv_start.setter
    def supv_start(self, value):
        self._supv_start = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainFinanceFsupvTaskQueryResponse, self).parse_response_content(response_content)
        if 'fund_supv_task_id' in response:
            self.fund_supv_task_id = response['fund_supv_task_id']
        if 'supervised_desensitized_access_no' in response:
            self.supervised_desensitized_access_no = response['supervised_desensitized_access_no']
        if 'supervised_special_account_no' in response:
            self.supervised_special_account_no = response['supervised_special_account_no']
        if 'supv_agreement_no' in response:
            self.supv_agreement_no = response['supv_agreement_no']
        if 'supv_end' in response:
            self.supv_end = response['supv_end']
        if 'supv_start' in response:
            self.supv_start = response['supv_start']
