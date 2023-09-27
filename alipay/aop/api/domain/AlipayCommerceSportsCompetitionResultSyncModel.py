#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceSportsCompetitionResultSyncModel(object):

    def __init__(self):
        self._bib = None
        self._competition_code = None
        self._competitor_code = None
        self._competitor_type = None
        self._composition_athletes = None
        self._data_version = None
        self._diff = None
        self._irm = None
        self._pty = None
        self._qualification_mark = None
        self._rank = None
        self._record_indicators = None
        self._result = None
        self._result_status = None
        self._result_type = None
        self._sort_order = None
        self._start_sort_order = None
        self._unit_code = None
        self._wlt = None

    @property
    def bib(self):
        return self._bib

    @bib.setter
    def bib(self, value):
        self._bib = value
    @property
    def competition_code(self):
        return self._competition_code

    @competition_code.setter
    def competition_code(self, value):
        self._competition_code = value
    @property
    def competitor_code(self):
        return self._competitor_code

    @competitor_code.setter
    def competitor_code(self, value):
        self._competitor_code = value
    @property
    def competitor_type(self):
        return self._competitor_type

    @competitor_type.setter
    def competitor_type(self, value):
        self._competitor_type = value
    @property
    def composition_athletes(self):
        return self._composition_athletes

    @composition_athletes.setter
    def composition_athletes(self, value):
        self._composition_athletes = value
    @property
    def data_version(self):
        return self._data_version

    @data_version.setter
    def data_version(self, value):
        self._data_version = value
    @property
    def diff(self):
        return self._diff

    @diff.setter
    def diff(self, value):
        self._diff = value
    @property
    def irm(self):
        return self._irm

    @irm.setter
    def irm(self, value):
        self._irm = value
    @property
    def pty(self):
        return self._pty

    @pty.setter
    def pty(self, value):
        self._pty = value
    @property
    def qualification_mark(self):
        return self._qualification_mark

    @qualification_mark.setter
    def qualification_mark(self, value):
        self._qualification_mark = value
    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, value):
        self._rank = value
    @property
    def record_indicators(self):
        return self._record_indicators

    @record_indicators.setter
    def record_indicators(self, value):
        self._record_indicators = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value
    @property
    def result_status(self):
        return self._result_status

    @result_status.setter
    def result_status(self, value):
        self._result_status = value
    @property
    def result_type(self):
        return self._result_type

    @result_type.setter
    def result_type(self, value):
        self._result_type = value
    @property
    def sort_order(self):
        return self._sort_order

    @sort_order.setter
    def sort_order(self, value):
        self._sort_order = value
    @property
    def start_sort_order(self):
        return self._start_sort_order

    @start_sort_order.setter
    def start_sort_order(self, value):
        self._start_sort_order = value
    @property
    def unit_code(self):
        return self._unit_code

    @unit_code.setter
    def unit_code(self, value):
        self._unit_code = value
    @property
    def wlt(self):
        return self._wlt

    @wlt.setter
    def wlt(self, value):
        self._wlt = value


    def to_alipay_dict(self):
        params = dict()
        if self.bib:
            if hasattr(self.bib, 'to_alipay_dict'):
                params['bib'] = self.bib.to_alipay_dict()
            else:
                params['bib'] = self.bib
        if self.competition_code:
            if hasattr(self.competition_code, 'to_alipay_dict'):
                params['competition_code'] = self.competition_code.to_alipay_dict()
            else:
                params['competition_code'] = self.competition_code
        if self.competitor_code:
            if hasattr(self.competitor_code, 'to_alipay_dict'):
                params['competitor_code'] = self.competitor_code.to_alipay_dict()
            else:
                params['competitor_code'] = self.competitor_code
        if self.competitor_type:
            if hasattr(self.competitor_type, 'to_alipay_dict'):
                params['competitor_type'] = self.competitor_type.to_alipay_dict()
            else:
                params['competitor_type'] = self.competitor_type
        if self.composition_athletes:
            if hasattr(self.composition_athletes, 'to_alipay_dict'):
                params['composition_athletes'] = self.composition_athletes.to_alipay_dict()
            else:
                params['composition_athletes'] = self.composition_athletes
        if self.data_version:
            if hasattr(self.data_version, 'to_alipay_dict'):
                params['data_version'] = self.data_version.to_alipay_dict()
            else:
                params['data_version'] = self.data_version
        if self.diff:
            if hasattr(self.diff, 'to_alipay_dict'):
                params['diff'] = self.diff.to_alipay_dict()
            else:
                params['diff'] = self.diff
        if self.irm:
            if hasattr(self.irm, 'to_alipay_dict'):
                params['irm'] = self.irm.to_alipay_dict()
            else:
                params['irm'] = self.irm
        if self.pty:
            if hasattr(self.pty, 'to_alipay_dict'):
                params['pty'] = self.pty.to_alipay_dict()
            else:
                params['pty'] = self.pty
        if self.qualification_mark:
            if hasattr(self.qualification_mark, 'to_alipay_dict'):
                params['qualification_mark'] = self.qualification_mark.to_alipay_dict()
            else:
                params['qualification_mark'] = self.qualification_mark
        if self.rank:
            if hasattr(self.rank, 'to_alipay_dict'):
                params['rank'] = self.rank.to_alipay_dict()
            else:
                params['rank'] = self.rank
        if self.record_indicators:
            if hasattr(self.record_indicators, 'to_alipay_dict'):
                params['record_indicators'] = self.record_indicators.to_alipay_dict()
            else:
                params['record_indicators'] = self.record_indicators
        if self.result:
            if hasattr(self.result, 'to_alipay_dict'):
                params['result'] = self.result.to_alipay_dict()
            else:
                params['result'] = self.result
        if self.result_status:
            if hasattr(self.result_status, 'to_alipay_dict'):
                params['result_status'] = self.result_status.to_alipay_dict()
            else:
                params['result_status'] = self.result_status
        if self.result_type:
            if hasattr(self.result_type, 'to_alipay_dict'):
                params['result_type'] = self.result_type.to_alipay_dict()
            else:
                params['result_type'] = self.result_type
        if self.sort_order:
            if hasattr(self.sort_order, 'to_alipay_dict'):
                params['sort_order'] = self.sort_order.to_alipay_dict()
            else:
                params['sort_order'] = self.sort_order
        if self.start_sort_order:
            if hasattr(self.start_sort_order, 'to_alipay_dict'):
                params['start_sort_order'] = self.start_sort_order.to_alipay_dict()
            else:
                params['start_sort_order'] = self.start_sort_order
        if self.unit_code:
            if hasattr(self.unit_code, 'to_alipay_dict'):
                params['unit_code'] = self.unit_code.to_alipay_dict()
            else:
                params['unit_code'] = self.unit_code
        if self.wlt:
            if hasattr(self.wlt, 'to_alipay_dict'):
                params['wlt'] = self.wlt.to_alipay_dict()
            else:
                params['wlt'] = self.wlt
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceSportsCompetitionResultSyncModel()
        if 'bib' in d:
            o.bib = d['bib']
        if 'competition_code' in d:
            o.competition_code = d['competition_code']
        if 'competitor_code' in d:
            o.competitor_code = d['competitor_code']
        if 'competitor_type' in d:
            o.competitor_type = d['competitor_type']
        if 'composition_athletes' in d:
            o.composition_athletes = d['composition_athletes']
        if 'data_version' in d:
            o.data_version = d['data_version']
        if 'diff' in d:
            o.diff = d['diff']
        if 'irm' in d:
            o.irm = d['irm']
        if 'pty' in d:
            o.pty = d['pty']
        if 'qualification_mark' in d:
            o.qualification_mark = d['qualification_mark']
        if 'rank' in d:
            o.rank = d['rank']
        if 'record_indicators' in d:
            o.record_indicators = d['record_indicators']
        if 'result' in d:
            o.result = d['result']
        if 'result_status' in d:
            o.result_status = d['result_status']
        if 'result_type' in d:
            o.result_type = d['result_type']
        if 'sort_order' in d:
            o.sort_order = d['sort_order']
        if 'start_sort_order' in d:
            o.start_sort_order = d['start_sort_order']
        if 'unit_code' in d:
            o.unit_code = d['unit_code']
        if 'wlt' in d:
            o.wlt = d['wlt']
        return o


