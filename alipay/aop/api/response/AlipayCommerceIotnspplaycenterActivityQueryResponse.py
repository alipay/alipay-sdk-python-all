#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.IotnspplaycenterActivityVoucherInfo import IotnspplaycenterActivityVoucherInfo


class AlipayCommerceIotnspplaycenterActivityQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotnspplaycenterActivityQueryResponse, self).__init__()
        self._act_status = None
        self._act_type = None
        self._activity_rule_detail = None
        self._card_logo = None
        self._card_text = None
        self._card_title = None
        self._current_progress = None
        self._gmt_expired = None
        self._gmt_start = None
        self._main_prize_image = None
        self._main_title = None
        self._progress_unit = None
        self._total_progress = None
        self._voucher_list = None

    @property
    def act_status(self):
        return self._act_status

    @act_status.setter
    def act_status(self, value):
        self._act_status = value
    @property
    def act_type(self):
        return self._act_type

    @act_type.setter
    def act_type(self, value):
        self._act_type = value
    @property
    def activity_rule_detail(self):
        return self._activity_rule_detail

    @activity_rule_detail.setter
    def activity_rule_detail(self, value):
        self._activity_rule_detail = value
    @property
    def card_logo(self):
        return self._card_logo

    @card_logo.setter
    def card_logo(self, value):
        self._card_logo = value
    @property
    def card_text(self):
        return self._card_text

    @card_text.setter
    def card_text(self, value):
        self._card_text = value
    @property
    def card_title(self):
        return self._card_title

    @card_title.setter
    def card_title(self, value):
        self._card_title = value
    @property
    def current_progress(self):
        return self._current_progress

    @current_progress.setter
    def current_progress(self, value):
        self._current_progress = value
    @property
    def gmt_expired(self):
        return self._gmt_expired

    @gmt_expired.setter
    def gmt_expired(self, value):
        self._gmt_expired = value
    @property
    def gmt_start(self):
        return self._gmt_start

    @gmt_start.setter
    def gmt_start(self, value):
        self._gmt_start = value
    @property
    def main_prize_image(self):
        return self._main_prize_image

    @main_prize_image.setter
    def main_prize_image(self, value):
        self._main_prize_image = value
    @property
    def main_title(self):
        return self._main_title

    @main_title.setter
    def main_title(self, value):
        self._main_title = value
    @property
    def progress_unit(self):
        return self._progress_unit

    @progress_unit.setter
    def progress_unit(self, value):
        self._progress_unit = value
    @property
    def total_progress(self):
        return self._total_progress

    @total_progress.setter
    def total_progress(self, value):
        self._total_progress = value
    @property
    def voucher_list(self):
        return self._voucher_list

    @voucher_list.setter
    def voucher_list(self, value):
        if isinstance(value, list):
            self._voucher_list = list()
            for i in value:
                if isinstance(i, IotnspplaycenterActivityVoucherInfo):
                    self._voucher_list.append(i)
                else:
                    self._voucher_list.append(IotnspplaycenterActivityVoucherInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotnspplaycenterActivityQueryResponse, self).parse_response_content(response_content)
        if 'act_status' in response:
            self.act_status = response['act_status']
        if 'act_type' in response:
            self.act_type = response['act_type']
        if 'activity_rule_detail' in response:
            self.activity_rule_detail = response['activity_rule_detail']
        if 'card_logo' in response:
            self.card_logo = response['card_logo']
        if 'card_text' in response:
            self.card_text = response['card_text']
        if 'card_title' in response:
            self.card_title = response['card_title']
        if 'current_progress' in response:
            self.current_progress = response['current_progress']
        if 'gmt_expired' in response:
            self.gmt_expired = response['gmt_expired']
        if 'gmt_start' in response:
            self.gmt_start = response['gmt_start']
        if 'main_prize_image' in response:
            self.main_prize_image = response['main_prize_image']
        if 'main_title' in response:
            self.main_title = response['main_title']
        if 'progress_unit' in response:
            self.progress_unit = response['progress_unit']
        if 'total_progress' in response:
            self.total_progress = response['total_progress']
        if 'voucher_list' in response:
            self.voucher_list = response['voucher_list']
