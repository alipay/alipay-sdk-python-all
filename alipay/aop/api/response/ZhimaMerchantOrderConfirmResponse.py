#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaMerchantOrderConfirmResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaMerchantOrderConfirmResponse, self).__init__()
        self._cert_no = None
        self._channel_id = None
        self._credit_amout = None
        self._ethnic_group = None
        self._house = None
        self._mobile = None
        self._name = None
        self._open_id = None
        self._user_id = None
        self._zm_face = None
        self._zm_grade = None
        self._zm_risk = None
        self._zm_score = None

    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def channel_id(self):
        return self._channel_id

    @channel_id.setter
    def channel_id(self, value):
        self._channel_id = value
    @property
    def credit_amout(self):
        return self._credit_amout

    @credit_amout.setter
    def credit_amout(self, value):
        self._credit_amout = value
    @property
    def ethnic_group(self):
        return self._ethnic_group

    @ethnic_group.setter
    def ethnic_group(self, value):
        self._ethnic_group = value
    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, value):
        self._house = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def zm_face(self):
        return self._zm_face

    @zm_face.setter
    def zm_face(self, value):
        self._zm_face = value
    @property
    def zm_grade(self):
        return self._zm_grade

    @zm_grade.setter
    def zm_grade(self, value):
        self._zm_grade = value
    @property
    def zm_risk(self):
        return self._zm_risk

    @zm_risk.setter
    def zm_risk(self, value):
        self._zm_risk = value
    @property
    def zm_score(self):
        return self._zm_score

    @zm_score.setter
    def zm_score(self, value):
        self._zm_score = value

    def parse_response_content(self, response_content):
        response = super(ZhimaMerchantOrderConfirmResponse, self).parse_response_content(response_content)
        if 'cert_no' in response:
            self.cert_no = response['cert_no']
        if 'channel_id' in response:
            self.channel_id = response['channel_id']
        if 'credit_amout' in response:
            self.credit_amout = response['credit_amout']
        if 'ethnic_group' in response:
            self.ethnic_group = response['ethnic_group']
        if 'house' in response:
            self.house = response['house']
        if 'mobile' in response:
            self.mobile = response['mobile']
        if 'name' in response:
            self.name = response['name']
        if 'open_id' in response:
            self.open_id = response['open_id']
        if 'user_id' in response:
            self.user_id = response['user_id']
        if 'zm_face' in response:
            self.zm_face = response['zm_face']
        if 'zm_grade' in response:
            self.zm_grade = response['zm_grade']
        if 'zm_risk' in response:
            self.zm_risk = response['zm_risk']
        if 'zm_score' in response:
            self.zm_score = response['zm_score']
