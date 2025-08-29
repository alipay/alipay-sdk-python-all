#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ResumeAttribute import ResumeAttribute
from alipay.aop.api.domain.UserIntentionInfo import UserIntentionInfo


class AlipayEbppIndustryJobResumeauthlogininfoGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryJobResumeauthlogininfoGetResponse, self).__init__()
        self._ad_code = None
        self._open_id = None
        self._out_biz_no = None
        self._resume_attributes = None
        self._user_id = None
        self._user_intention_info = None

    @property
    def ad_code(self):
        return self._ad_code

    @ad_code.setter
    def ad_code(self, value):
        self._ad_code = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def resume_attributes(self):
        return self._resume_attributes

    @resume_attributes.setter
    def resume_attributes(self, value):
        if isinstance(value, list):
            self._resume_attributes = list()
            for i in value:
                if isinstance(i, ResumeAttribute):
                    self._resume_attributes.append(i)
                else:
                    self._resume_attributes.append(ResumeAttribute.from_alipay_dict(i))
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_intention_info(self):
        return self._user_intention_info

    @user_intention_info.setter
    def user_intention_info(self, value):
        if isinstance(value, UserIntentionInfo):
            self._user_intention_info = value
        else:
            self._user_intention_info = UserIntentionInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryJobResumeauthlogininfoGetResponse, self).parse_response_content(response_content)
        if 'ad_code' in response:
            self.ad_code = response['ad_code']
        if 'open_id' in response:
            self.open_id = response['open_id']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'resume_attributes' in response:
            self.resume_attributes = response['resume_attributes']
        if 'user_id' in response:
            self.user_id = response['user_id']
        if 'user_intention_info' in response:
            self.user_intention_info = response['user_intention_info']
