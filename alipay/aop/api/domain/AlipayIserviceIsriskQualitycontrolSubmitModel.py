#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OfflineTextQc import OfflineTextQc
from alipay.aop.api.domain.RealtimeTextQc import RealtimeTextQc


class AlipayIserviceIsriskQualitycontrolSubmitModel(object):

    def __init__(self):
        self._biz_id = None
        self._function_type = None
        self._instance_code = None
        self._nebula_id = None
        self._offline_text_qc = None
        self._realtime_text_qc = None
        self._recording_urls = None
        self._skill_group_id = None
        self._skill_group_type = None
        self._tnt_inst_id = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def function_type(self):
        return self._function_type

    @function_type.setter
    def function_type(self, value):
        self._function_type = value
    @property
    def instance_code(self):
        return self._instance_code

    @instance_code.setter
    def instance_code(self, value):
        self._instance_code = value
    @property
    def nebula_id(self):
        return self._nebula_id

    @nebula_id.setter
    def nebula_id(self, value):
        self._nebula_id = value
    @property
    def offline_text_qc(self):
        return self._offline_text_qc

    @offline_text_qc.setter
    def offline_text_qc(self, value):
        if isinstance(value, OfflineTextQc):
            self._offline_text_qc = value
        else:
            self._offline_text_qc = OfflineTextQc.from_alipay_dict(value)
    @property
    def realtime_text_qc(self):
        return self._realtime_text_qc

    @realtime_text_qc.setter
    def realtime_text_qc(self, value):
        if isinstance(value, RealtimeTextQc):
            self._realtime_text_qc = value
        else:
            self._realtime_text_qc = RealtimeTextQc.from_alipay_dict(value)
    @property
    def recording_urls(self):
        return self._recording_urls

    @recording_urls.setter
    def recording_urls(self, value):
        if isinstance(value, list):
            self._recording_urls = list()
            for i in value:
                self._recording_urls.append(i)
    @property
    def skill_group_id(self):
        return self._skill_group_id

    @skill_group_id.setter
    def skill_group_id(self, value):
        self._skill_group_id = value
    @property
    def skill_group_type(self):
        return self._skill_group_type

    @skill_group_type.setter
    def skill_group_type(self, value):
        self._skill_group_type = value
    @property
    def tnt_inst_id(self):
        return self._tnt_inst_id

    @tnt_inst_id.setter
    def tnt_inst_id(self, value):
        self._tnt_inst_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.function_type:
            if hasattr(self.function_type, 'to_alipay_dict'):
                params['function_type'] = self.function_type.to_alipay_dict()
            else:
                params['function_type'] = self.function_type
        if self.instance_code:
            if hasattr(self.instance_code, 'to_alipay_dict'):
                params['instance_code'] = self.instance_code.to_alipay_dict()
            else:
                params['instance_code'] = self.instance_code
        if self.nebula_id:
            if hasattr(self.nebula_id, 'to_alipay_dict'):
                params['nebula_id'] = self.nebula_id.to_alipay_dict()
            else:
                params['nebula_id'] = self.nebula_id
        if self.offline_text_qc:
            if hasattr(self.offline_text_qc, 'to_alipay_dict'):
                params['offline_text_qc'] = self.offline_text_qc.to_alipay_dict()
            else:
                params['offline_text_qc'] = self.offline_text_qc
        if self.realtime_text_qc:
            if hasattr(self.realtime_text_qc, 'to_alipay_dict'):
                params['realtime_text_qc'] = self.realtime_text_qc.to_alipay_dict()
            else:
                params['realtime_text_qc'] = self.realtime_text_qc
        if self.recording_urls:
            if isinstance(self.recording_urls, list):
                for i in range(0, len(self.recording_urls)):
                    element = self.recording_urls[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.recording_urls[i] = element.to_alipay_dict()
            if hasattr(self.recording_urls, 'to_alipay_dict'):
                params['recording_urls'] = self.recording_urls.to_alipay_dict()
            else:
                params['recording_urls'] = self.recording_urls
        if self.skill_group_id:
            if hasattr(self.skill_group_id, 'to_alipay_dict'):
                params['skill_group_id'] = self.skill_group_id.to_alipay_dict()
            else:
                params['skill_group_id'] = self.skill_group_id
        if self.skill_group_type:
            if hasattr(self.skill_group_type, 'to_alipay_dict'):
                params['skill_group_type'] = self.skill_group_type.to_alipay_dict()
            else:
                params['skill_group_type'] = self.skill_group_type
        if self.tnt_inst_id:
            if hasattr(self.tnt_inst_id, 'to_alipay_dict'):
                params['tnt_inst_id'] = self.tnt_inst_id.to_alipay_dict()
            else:
                params['tnt_inst_id'] = self.tnt_inst_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceIsriskQualitycontrolSubmitModel()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'function_type' in d:
            o.function_type = d['function_type']
        if 'instance_code' in d:
            o.instance_code = d['instance_code']
        if 'nebula_id' in d:
            o.nebula_id = d['nebula_id']
        if 'offline_text_qc' in d:
            o.offline_text_qc = d['offline_text_qc']
        if 'realtime_text_qc' in d:
            o.realtime_text_qc = d['realtime_text_qc']
        if 'recording_urls' in d:
            o.recording_urls = d['recording_urls']
        if 'skill_group_id' in d:
            o.skill_group_id = d['skill_group_id']
        if 'skill_group_type' in d:
            o.skill_group_type = d['skill_group_type']
        if 'tnt_inst_id' in d:
            o.tnt_inst_id = d['tnt_inst_id']
        return o


