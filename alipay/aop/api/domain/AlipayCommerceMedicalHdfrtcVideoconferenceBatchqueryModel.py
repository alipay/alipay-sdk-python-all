#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalHdfrtcVideoconferenceBatchqueryModel(object):

    def __init__(self):
        self._video_conference_id_list = None

    @property
    def video_conference_id_list(self):
        return self._video_conference_id_list

    @video_conference_id_list.setter
    def video_conference_id_list(self, value):
        if isinstance(value, list):
            self._video_conference_id_list = list()
            for i in value:
                self._video_conference_id_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.video_conference_id_list:
            if isinstance(self.video_conference_id_list, list):
                for i in range(0, len(self.video_conference_id_list)):
                    element = self.video_conference_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.video_conference_id_list[i] = element.to_alipay_dict()
            if hasattr(self.video_conference_id_list, 'to_alipay_dict'):
                params['video_conference_id_list'] = self.video_conference_id_list.to_alipay_dict()
            else:
                params['video_conference_id_list'] = self.video_conference_id_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalHdfrtcVideoconferenceBatchqueryModel()
        if 'video_conference_id_list' in d:
            o.video_conference_id_list = d['video_conference_id_list']
        return o


