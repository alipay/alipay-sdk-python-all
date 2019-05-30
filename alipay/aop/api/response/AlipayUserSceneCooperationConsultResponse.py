#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MemberBenefitInfo import MemberBenefitInfo


class AlipayUserSceneCooperationConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserSceneCooperationConsultResponse, self).__init__()
        self._alipay_logon_id = None
        self._app_new = None
        self._benefit_info_list = None
        self._consult_result = None
        self._invite_result = None

    @property
    def alipay_logon_id(self):
        return self._alipay_logon_id

    @alipay_logon_id.setter
    def alipay_logon_id(self, value):
        self._alipay_logon_id = value
    @property
    def app_new(self):
        return self._app_new

    @app_new.setter
    def app_new(self, value):
        self._app_new = value
    @property
    def benefit_info_list(self):
        return self._benefit_info_list

    @benefit_info_list.setter
    def benefit_info_list(self, value):
        if isinstance(value, list):
            self._benefit_info_list = list()
            for i in value:
                if isinstance(i, MemberBenefitInfo):
                    self._benefit_info_list.append(i)
                else:
                    self._benefit_info_list.append(MemberBenefitInfo.from_alipay_dict(i))
    @property
    def consult_result(self):
        return self._consult_result

    @consult_result.setter
    def consult_result(self, value):
        self._consult_result = value
    @property
    def invite_result(self):
        return self._invite_result

    @invite_result.setter
    def invite_result(self, value):
        self._invite_result = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserSceneCooperationConsultResponse, self).parse_response_content(response_content)
        if 'alipay_logon_id' in response:
            self.alipay_logon_id = response['alipay_logon_id']
        if 'app_new' in response:
            self.app_new = response['app_new']
        if 'benefit_info_list' in response:
            self.benefit_info_list = response['benefit_info_list']
        if 'consult_result' in response:
            self.consult_result = response['consult_result']
        if 'invite_result' in response:
            self.invite_result = response['invite_result']
