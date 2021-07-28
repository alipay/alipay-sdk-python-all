#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BigCardData import BigCardData
from alipay.aop.api.domain.BigCardData import BigCardData


class AlipayUserMemberAlipaybigcardQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserMemberAlipaybigcardQueryResponse, self).__init__()
        self._alipay_big_card_cache_data = None
        self._alipay_big_card_real_time_data = None
        self._backup_display_info = None
        self._backup_template_code = None
        self._backup_track_info = None
        self._display_info = None
        self._ext_info = None
        self._result_code = None
        self._result_desc = None
        self._retryable = None
        self._success = None
        self._template_code = None
        self._track_info = None

    @property
    def alipay_big_card_cache_data(self):
        return self._alipay_big_card_cache_data

    @alipay_big_card_cache_data.setter
    def alipay_big_card_cache_data(self, value):
        if isinstance(value, BigCardData):
            self._alipay_big_card_cache_data = value
        else:
            self._alipay_big_card_cache_data = BigCardData.from_alipay_dict(value)
    @property
    def alipay_big_card_real_time_data(self):
        return self._alipay_big_card_real_time_data

    @alipay_big_card_real_time_data.setter
    def alipay_big_card_real_time_data(self, value):
        if isinstance(value, BigCardData):
            self._alipay_big_card_real_time_data = value
        else:
            self._alipay_big_card_real_time_data = BigCardData.from_alipay_dict(value)
    @property
    def backup_display_info(self):
        return self._backup_display_info

    @backup_display_info.setter
    def backup_display_info(self, value):
        self._backup_display_info = value
    @property
    def backup_template_code(self):
        return self._backup_template_code

    @backup_template_code.setter
    def backup_template_code(self, value):
        self._backup_template_code = value
    @property
    def backup_track_info(self):
        return self._backup_track_info

    @backup_track_info.setter
    def backup_track_info(self, value):
        self._backup_track_info = value
    @property
    def display_info(self):
        return self._display_info

    @display_info.setter
    def display_info(self, value):
        self._display_info = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def result_desc(self):
        return self._result_desc

    @result_desc.setter
    def result_desc(self, value):
        self._result_desc = value
    @property
    def retryable(self):
        return self._retryable

    @retryable.setter
    def retryable(self, value):
        self._retryable = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value
    @property
    def template_code(self):
        return self._template_code

    @template_code.setter
    def template_code(self, value):
        self._template_code = value
    @property
    def track_info(self):
        return self._track_info

    @track_info.setter
    def track_info(self, value):
        self._track_info = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserMemberAlipaybigcardQueryResponse, self).parse_response_content(response_content)
        if 'alipay_big_card_cache_data' in response:
            self.alipay_big_card_cache_data = response['alipay_big_card_cache_data']
        if 'alipay_big_card_real_time_data' in response:
            self.alipay_big_card_real_time_data = response['alipay_big_card_real_time_data']
        if 'backup_display_info' in response:
            self.backup_display_info = response['backup_display_info']
        if 'backup_template_code' in response:
            self.backup_template_code = response['backup_template_code']
        if 'backup_track_info' in response:
            self.backup_track_info = response['backup_track_info']
        if 'display_info' in response:
            self.display_info = response['display_info']
        if 'ext_info' in response:
            self.ext_info = response['ext_info']
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'result_desc' in response:
            self.result_desc = response['result_desc']
        if 'retryable' in response:
            self.retryable = response['retryable']
        if 'success' in response:
            self.success = response['success']
        if 'template_code' in response:
            self.template_code = response['template_code']
        if 'track_info' in response:
            self.track_info = response['track_info']
