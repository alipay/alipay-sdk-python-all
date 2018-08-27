#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KbAdvertSubjectResponse import KbAdvertSubjectResponse


class KbAdvertMissionResponse(object):

    def __init__(self):
        self._gmt_claimed = None
        self._gmt_end = None
        self._gmt_start = None
        self._mission_id = None
        self._promote_status = None
        self._subjects = None

    @property
    def gmt_claimed(self):
        return self._gmt_claimed

    @gmt_claimed.setter
    def gmt_claimed(self, value):
        self._gmt_claimed = value
    @property
    def gmt_end(self):
        return self._gmt_end

    @gmt_end.setter
    def gmt_end(self, value):
        self._gmt_end = value
    @property
    def gmt_start(self):
        return self._gmt_start

    @gmt_start.setter
    def gmt_start(self, value):
        self._gmt_start = value
    @property
    def mission_id(self):
        return self._mission_id

    @mission_id.setter
    def mission_id(self, value):
        self._mission_id = value
    @property
    def promote_status(self):
        return self._promote_status

    @promote_status.setter
    def promote_status(self, value):
        self._promote_status = value
    @property
    def subjects(self):
        return self._subjects

    @subjects.setter
    def subjects(self, value):
        if isinstance(value, list):
            self._subjects = list()
            for i in value:
                if isinstance(i, KbAdvertSubjectResponse):
                    self._subjects.append(i)
                else:
                    self._subjects.append(KbAdvertSubjectResponse.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.gmt_claimed:
            if hasattr(self.gmt_claimed, 'to_alipay_dict'):
                params['gmt_claimed'] = self.gmt_claimed.to_alipay_dict()
            else:
                params['gmt_claimed'] = self.gmt_claimed
        if self.gmt_end:
            if hasattr(self.gmt_end, 'to_alipay_dict'):
                params['gmt_end'] = self.gmt_end.to_alipay_dict()
            else:
                params['gmt_end'] = self.gmt_end
        if self.gmt_start:
            if hasattr(self.gmt_start, 'to_alipay_dict'):
                params['gmt_start'] = self.gmt_start.to_alipay_dict()
            else:
                params['gmt_start'] = self.gmt_start
        if self.mission_id:
            if hasattr(self.mission_id, 'to_alipay_dict'):
                params['mission_id'] = self.mission_id.to_alipay_dict()
            else:
                params['mission_id'] = self.mission_id
        if self.promote_status:
            if hasattr(self.promote_status, 'to_alipay_dict'):
                params['promote_status'] = self.promote_status.to_alipay_dict()
            else:
                params['promote_status'] = self.promote_status
        if self.subjects:
            if isinstance(self.subjects, list):
                for i in range(0, len(self.subjects)):
                    element = self.subjects[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.subjects[i] = element.to_alipay_dict()
            if hasattr(self.subjects, 'to_alipay_dict'):
                params['subjects'] = self.subjects.to_alipay_dict()
            else:
                params['subjects'] = self.subjects
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbAdvertMissionResponse()
        if 'gmt_claimed' in d:
            o.gmt_claimed = d['gmt_claimed']
        if 'gmt_end' in d:
            o.gmt_end = d['gmt_end']
        if 'gmt_start' in d:
            o.gmt_start = d['gmt_start']
        if 'mission_id' in d:
            o.mission_id = d['mission_id']
        if 'promote_status' in d:
            o.promote_status = d['promote_status']
        if 'subjects' in d:
            o.subjects = d['subjects']
        return o


