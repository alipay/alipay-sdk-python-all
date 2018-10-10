#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditHuabeiAuthOrderUnfreezeResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditHuabeiAuthOrderUnfreezeResponse, self).__init__()
        self._agreement_no = None
        self._agreement_status = None
        self._alipay_user_id = None
        self._auth_opt_id = None
        self._gmt_trans = None
        self._out_request_no = None
        self._rest_freeze_amount = None
        self._seller_id = None
        self._trans_status = None
        self._unfreeze_amount = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def agreement_status(self):
        return self._agreement_status

    @agreement_status.setter
    def agreement_status(self, value):
        self._agreement_status = value
    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def auth_opt_id(self):
        return self._auth_opt_id

    @auth_opt_id.setter
    def auth_opt_id(self, value):
        self._auth_opt_id = value
    @property
    def gmt_trans(self):
        return self._gmt_trans

    @gmt_trans.setter
    def gmt_trans(self, value):
        self._gmt_trans = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def rest_freeze_amount(self):
        return self._rest_freeze_amount

    @rest_freeze_amount.setter
    def rest_freeze_amount(self, value):
        self._rest_freeze_amount = value
    @property
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value
    @property
    def trans_status(self):
        return self._trans_status

    @trans_status.setter
    def trans_status(self, value):
        self._trans_status = value
    @property
    def unfreeze_amount(self):
        return self._unfreeze_amount

    @unfreeze_amount.setter
    def unfreeze_amount(self, value):
        self._unfreeze_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditHuabeiAuthOrderUnfreezeResponse, self).parse_response_content(response_content)
        if 'agreement_no' in response:
            self.agreement_no = response['agreement_no']
        if 'agreement_status' in response:
            self.agreement_status = response['agreement_status']
        if 'alipay_user_id' in response:
            self.alipay_user_id = response['alipay_user_id']
        if 'auth_opt_id' in response:
            self.auth_opt_id = response['auth_opt_id']
        if 'gmt_trans' in response:
            self.gmt_trans = response['gmt_trans']
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
        if 'rest_freeze_amount' in response:
            self.rest_freeze_amount = response['rest_freeze_amount']
        if 'seller_id' in response:
            self.seller_id = response['seller_id']
        if 'trans_status' in response:
            self.trans_status = response['trans_status']
        if 'unfreeze_amount' in response:
            self.unfreeze_amount = response['unfreeze_amount']
