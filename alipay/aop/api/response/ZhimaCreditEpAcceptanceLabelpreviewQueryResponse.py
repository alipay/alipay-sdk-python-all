#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EpLabelContent import EpLabelContent


class ZhimaCreditEpAcceptanceLabelpreviewQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpAcceptanceLabelpreviewQueryResponse, self).__init__()
        self._has_authed = None
        self._has_data = None
        self._label_content = None
        self._label_count = None
        self._label_show_type = None
        self._label_to_obtain_count = None

    @property
    def has_authed(self):
        return self._has_authed

    @has_authed.setter
    def has_authed(self, value):
        self._has_authed = value
    @property
    def has_data(self):
        return self._has_data

    @has_data.setter
    def has_data(self, value):
        self._has_data = value
    @property
    def label_content(self):
        return self._label_content

    @label_content.setter
    def label_content(self, value):
        if isinstance(value, list):
            self._label_content = list()
            for i in value:
                if isinstance(i, EpLabelContent):
                    self._label_content.append(i)
                else:
                    self._label_content.append(EpLabelContent.from_alipay_dict(i))
    @property
    def label_count(self):
        return self._label_count

    @label_count.setter
    def label_count(self, value):
        self._label_count = value
    @property
    def label_show_type(self):
        return self._label_show_type

    @label_show_type.setter
    def label_show_type(self, value):
        self._label_show_type = value
    @property
    def label_to_obtain_count(self):
        return self._label_to_obtain_count

    @label_to_obtain_count.setter
    def label_to_obtain_count(self, value):
        self._label_to_obtain_count = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpAcceptanceLabelpreviewQueryResponse, self).parse_response_content(response_content)
        if 'has_authed' in response:
            self.has_authed = response['has_authed']
        if 'has_data' in response:
            self.has_data = response['has_data']
        if 'label_content' in response:
            self.label_content = response['label_content']
        if 'label_count' in response:
            self.label_count = response['label_count']
        if 'label_show_type' in response:
            self.label_show_type = response['label_show_type']
        if 'label_to_obtain_count' in response:
            self.label_to_obtain_count = response['label_to_obtain_count']
