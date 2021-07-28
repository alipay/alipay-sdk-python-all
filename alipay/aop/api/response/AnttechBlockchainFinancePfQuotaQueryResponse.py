#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechBlockchainFinancePfQuotaQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainFinancePfQuotaQueryResponse, self).__init__()
        self._agrm_bk_no = None
        self._cr_limit = None
        self._lmt_no = None
        self._lmt_status = None
        self._parm = None
        self._remain_limit = None
        self._trans_no = None

    @property
    def agrm_bk_no(self):
        return self._agrm_bk_no

    @agrm_bk_no.setter
    def agrm_bk_no(self, value):
        self._agrm_bk_no = value
    @property
    def cr_limit(self):
        return self._cr_limit

    @cr_limit.setter
    def cr_limit(self, value):
        self._cr_limit = value
    @property
    def lmt_no(self):
        return self._lmt_no

    @lmt_no.setter
    def lmt_no(self, value):
        self._lmt_no = value
    @property
    def lmt_status(self):
        return self._lmt_status

    @lmt_status.setter
    def lmt_status(self, value):
        self._lmt_status = value
    @property
    def parm(self):
        return self._parm

    @parm.setter
    def parm(self, value):
        self._parm = value
    @property
    def remain_limit(self):
        return self._remain_limit

    @remain_limit.setter
    def remain_limit(self, value):
        self._remain_limit = value
    @property
    def trans_no(self):
        return self._trans_no

    @trans_no.setter
    def trans_no(self, value):
        self._trans_no = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainFinancePfQuotaQueryResponse, self).parse_response_content(response_content)
        if 'agrm_bk_no' in response:
            self.agrm_bk_no = response['agrm_bk_no']
        if 'cr_limit' in response:
            self.cr_limit = response['cr_limit']
        if 'lmt_no' in response:
            self.lmt_no = response['lmt_no']
        if 'lmt_status' in response:
            self.lmt_status = response['lmt_status']
        if 'parm' in response:
            self.parm = response['parm']
        if 'remain_limit' in response:
            self.remain_limit = response['remain_limit']
        if 'trans_no' in response:
            self.trans_no = response['trans_no']
