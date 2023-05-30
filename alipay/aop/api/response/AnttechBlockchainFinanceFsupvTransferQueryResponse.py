#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SupvFundTransferDetail import SupvFundTransferDetail


class AnttechBlockchainFinanceFsupvTransferQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainFinanceFsupvTransferQueryResponse, self).__init__()
        self._fund_supv_task_id = None
        self._supv_special_account_no = None
        self._transfer_desc = None
        self._transfer_detail = None
        self._transfer_status = None

    @property
    def fund_supv_task_id(self):
        return self._fund_supv_task_id

    @fund_supv_task_id.setter
    def fund_supv_task_id(self, value):
        self._fund_supv_task_id = value
    @property
    def supv_special_account_no(self):
        return self._supv_special_account_no

    @supv_special_account_no.setter
    def supv_special_account_no(self, value):
        self._supv_special_account_no = value
    @property
    def transfer_desc(self):
        return self._transfer_desc

    @transfer_desc.setter
    def transfer_desc(self, value):
        self._transfer_desc = value
    @property
    def transfer_detail(self):
        return self._transfer_detail

    @transfer_detail.setter
    def transfer_detail(self, value):
        if isinstance(value, list):
            self._transfer_detail = list()
            for i in value:
                if isinstance(i, SupvFundTransferDetail):
                    self._transfer_detail.append(i)
                else:
                    self._transfer_detail.append(SupvFundTransferDetail.from_alipay_dict(i))
    @property
    def transfer_status(self):
        return self._transfer_status

    @transfer_status.setter
    def transfer_status(self, value):
        self._transfer_status = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainFinanceFsupvTransferQueryResponse, self).parse_response_content(response_content)
        if 'fund_supv_task_id' in response:
            self.fund_supv_task_id = response['fund_supv_task_id']
        if 'supv_special_account_no' in response:
            self.supv_special_account_no = response['supv_special_account_no']
        if 'transfer_desc' in response:
            self.transfer_desc = response['transfer_desc']
        if 'transfer_detail' in response:
            self.transfer_detail = response['transfer_detail']
        if 'transfer_status' in response:
            self.transfer_status = response['transfer_status']
