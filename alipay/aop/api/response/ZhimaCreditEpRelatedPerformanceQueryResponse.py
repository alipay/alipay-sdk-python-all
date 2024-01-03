#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PenCaseInfo import PenCaseInfo
from alipay.aop.api.domain.PunishBreakInfo import PunishBreakInfo
from alipay.aop.api.domain.PunishedInfo import PunishedInfo
from alipay.aop.api.domain.RelatedPerformanceInfo import RelatedPerformanceInfo
from alipay.aop.api.domain.RelatedPerformanceInfo import RelatedPerformanceInfo
from alipay.aop.api.domain.RelatedPerformanceInfo import RelatedPerformanceInfo


class ZhimaCreditEpRelatedPerformanceQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpRelatedPerformanceQueryResponse, self).__init__()
        self._case_info_list = None
        self._is_verified = None
        self._punish_break_list = None
        self._punished_list = None
        self._ry_pos_fr_list = None
        self._ry_pos_per_list = None
        self._ry_pos_sha_list = None

    @property
    def case_info_list(self):
        return self._case_info_list

    @case_info_list.setter
    def case_info_list(self, value):
        if isinstance(value, list):
            self._case_info_list = list()
            for i in value:
                if isinstance(i, PenCaseInfo):
                    self._case_info_list.append(i)
                else:
                    self._case_info_list.append(PenCaseInfo.from_alipay_dict(i))
    @property
    def is_verified(self):
        return self._is_verified

    @is_verified.setter
    def is_verified(self, value):
        self._is_verified = value
    @property
    def punish_break_list(self):
        return self._punish_break_list

    @punish_break_list.setter
    def punish_break_list(self, value):
        if isinstance(value, list):
            self._punish_break_list = list()
            for i in value:
                if isinstance(i, PunishBreakInfo):
                    self._punish_break_list.append(i)
                else:
                    self._punish_break_list.append(PunishBreakInfo.from_alipay_dict(i))
    @property
    def punished_list(self):
        return self._punished_list

    @punished_list.setter
    def punished_list(self, value):
        if isinstance(value, list):
            self._punished_list = list()
            for i in value:
                if isinstance(i, PunishedInfo):
                    self._punished_list.append(i)
                else:
                    self._punished_list.append(PunishedInfo.from_alipay_dict(i))
    @property
    def ry_pos_fr_list(self):
        return self._ry_pos_fr_list

    @ry_pos_fr_list.setter
    def ry_pos_fr_list(self, value):
        if isinstance(value, list):
            self._ry_pos_fr_list = list()
            for i in value:
                if isinstance(i, RelatedPerformanceInfo):
                    self._ry_pos_fr_list.append(i)
                else:
                    self._ry_pos_fr_list.append(RelatedPerformanceInfo.from_alipay_dict(i))
    @property
    def ry_pos_per_list(self):
        return self._ry_pos_per_list

    @ry_pos_per_list.setter
    def ry_pos_per_list(self, value):
        if isinstance(value, list):
            self._ry_pos_per_list = list()
            for i in value:
                if isinstance(i, RelatedPerformanceInfo):
                    self._ry_pos_per_list.append(i)
                else:
                    self._ry_pos_per_list.append(RelatedPerformanceInfo.from_alipay_dict(i))
    @property
    def ry_pos_sha_list(self):
        return self._ry_pos_sha_list

    @ry_pos_sha_list.setter
    def ry_pos_sha_list(self, value):
        if isinstance(value, list):
            self._ry_pos_sha_list = list()
            for i in value:
                if isinstance(i, RelatedPerformanceInfo):
                    self._ry_pos_sha_list.append(i)
                else:
                    self._ry_pos_sha_list.append(RelatedPerformanceInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpRelatedPerformanceQueryResponse, self).parse_response_content(response_content)
        if 'case_info_list' in response:
            self.case_info_list = response['case_info_list']
        if 'is_verified' in response:
            self.is_verified = response['is_verified']
        if 'punish_break_list' in response:
            self.punish_break_list = response['punish_break_list']
        if 'punished_list' in response:
            self.punished_list = response['punished_list']
        if 'ry_pos_fr_list' in response:
            self.ry_pos_fr_list = response['ry_pos_fr_list']
        if 'ry_pos_per_list' in response:
            self.ry_pos_per_list = response['ry_pos_per_list']
        if 'ry_pos_sha_list' in response:
            self.ry_pos_sha_list = response['ry_pos_sha_list']
