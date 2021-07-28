#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditHuabeiAuthAgreementQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditHuabeiAuthAgreementQueryResponse, self).__init__()
        self._agreement_name = None
        self._agreement_no = None
        self._agreement_status = None
        self._alipay_user_id = None
        self._auth_scene = None
        self._external_logon_id = None
        self._gmt_sign = None
        self._gmt_unsign = None
        self._out_biz_type = None
        self._out_sign_no = None
        self._rest_freeze_amount = None

    @property
    def agreement_name(self):
        return self._agreement_name

    @agreement_name.setter
    def agreement_name(self, value):
        self._agreement_name = value
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
    def auth_scene(self):
        return self._auth_scene

    @auth_scene.setter
    def auth_scene(self, value):
        self._auth_scene = value
    @property
    def external_logon_id(self):
        return self._external_logon_id

    @external_logon_id.setter
    def external_logon_id(self, value):
        self._external_logon_id = value
    @property
    def gmt_sign(self):
        return self._gmt_sign

    @gmt_sign.setter
    def gmt_sign(self, value):
        self._gmt_sign = value
    @property
    def gmt_unsign(self):
        return self._gmt_unsign

    @gmt_unsign.setter
    def gmt_unsign(self, value):
        self._gmt_unsign = value
    @property
    def out_biz_type(self):
        return self._out_biz_type

    @out_biz_type.setter
    def out_biz_type(self, value):
        self._out_biz_type = value
    @property
    def out_sign_no(self):
        return self._out_sign_no

    @out_sign_no.setter
    def out_sign_no(self, value):
        self._out_sign_no = value
    @property
    def rest_freeze_amount(self):
        return self._rest_freeze_amount

    @rest_freeze_amount.setter
    def rest_freeze_amount(self, value):
        self._rest_freeze_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditHuabeiAuthAgreementQueryResponse, self).parse_response_content(response_content)
        if 'agreement_name' in response:
            self.agreement_name = response['agreement_name']
        if 'agreement_no' in response:
            self.agreement_no = response['agreement_no']
        if 'agreement_status' in response:
            self.agreement_status = response['agreement_status']
        if 'alipay_user_id' in response:
            self.alipay_user_id = response['alipay_user_id']
        if 'auth_scene' in response:
            self.auth_scene = response['auth_scene']
        if 'external_logon_id' in response:
            self.external_logon_id = response['external_logon_id']
        if 'gmt_sign' in response:
            self.gmt_sign = response['gmt_sign']
        if 'gmt_unsign' in response:
            self.gmt_unsign = response['gmt_unsign']
        if 'out_biz_type' in response:
            self.out_biz_type = response['out_biz_type']
        if 'out_sign_no' in response:
            self.out_sign_no = response['out_sign_no']
        if 'rest_freeze_amount' in response:
            self.rest_freeze_amount = response['rest_freeze_amount']
