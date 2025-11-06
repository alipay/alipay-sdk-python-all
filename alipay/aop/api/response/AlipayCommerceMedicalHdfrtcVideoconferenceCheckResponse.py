#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RemindTextInfo import RemindTextInfo


class AlipayCommerceMedicalHdfrtcVideoconferenceCheckResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalHdfrtcVideoconferenceCheckResponse, self).__init__()
        self._can_enter = None
        self._party_entered_tips = None
        self._remind_text_list = None
        self._title = None

    @property
    def can_enter(self):
        return self._can_enter

    @can_enter.setter
    def can_enter(self, value):
        self._can_enter = value
    @property
    def party_entered_tips(self):
        return self._party_entered_tips

    @party_entered_tips.setter
    def party_entered_tips(self, value):
        self._party_entered_tips = value
    @property
    def remind_text_list(self):
        return self._remind_text_list

    @remind_text_list.setter
    def remind_text_list(self, value):
        if isinstance(value, list):
            self._remind_text_list = list()
            for i in value:
                if isinstance(i, RemindTextInfo):
                    self._remind_text_list.append(i)
                else:
                    self._remind_text_list.append(RemindTextInfo.from_alipay_dict(i))
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalHdfrtcVideoconferenceCheckResponse, self).parse_response_content(response_content)
        if 'can_enter' in response:
            self.can_enter = response['can_enter']
        if 'party_entered_tips' in response:
            self.party_entered_tips = response['party_entered_tips']
        if 'remind_text_list' in response:
            self.remind_text_list = response['remind_text_list']
        if 'title' in response:
            self.title = response['title']
