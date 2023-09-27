#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceSportsCompetitionScheduleSyncModel(object):

    def __init__(self):
        self._actual_end_date = None
        self._actual_start_date = None
        self._cn_name = None
        self._competition_code = None
        self._data_version = None
        self._discipline = None
        self._en_name = None
        self._end_date = None
        self._event_unit_type = None
        self._hot_label = None
        self._hot_level = None
        self._location_code = None
        self._location_name = None
        self._medal_flag = None
        self._schedule_status = None
        self._start_date = None
        self._unit_code = None
        self._venue_code = None
        self._venue_name = None

    @property
    def actual_end_date(self):
        return self._actual_end_date

    @actual_end_date.setter
    def actual_end_date(self, value):
        self._actual_end_date = value
    @property
    def actual_start_date(self):
        return self._actual_start_date

    @actual_start_date.setter
    def actual_start_date(self, value):
        self._actual_start_date = value
    @property
    def cn_name(self):
        return self._cn_name

    @cn_name.setter
    def cn_name(self, value):
        self._cn_name = value
    @property
    def competition_code(self):
        return self._competition_code

    @competition_code.setter
    def competition_code(self, value):
        self._competition_code = value
    @property
    def data_version(self):
        return self._data_version

    @data_version.setter
    def data_version(self, value):
        self._data_version = value
    @property
    def discipline(self):
        return self._discipline

    @discipline.setter
    def discipline(self, value):
        self._discipline = value
    @property
    def en_name(self):
        return self._en_name

    @en_name.setter
    def en_name(self, value):
        self._en_name = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def event_unit_type(self):
        return self._event_unit_type

    @event_unit_type.setter
    def event_unit_type(self, value):
        self._event_unit_type = value
    @property
    def hot_label(self):
        return self._hot_label

    @hot_label.setter
    def hot_label(self, value):
        self._hot_label = value
    @property
    def hot_level(self):
        return self._hot_level

    @hot_level.setter
    def hot_level(self, value):
        self._hot_level = value
    @property
    def location_code(self):
        return self._location_code

    @location_code.setter
    def location_code(self, value):
        self._location_code = value
    @property
    def location_name(self):
        return self._location_name

    @location_name.setter
    def location_name(self, value):
        self._location_name = value
    @property
    def medal_flag(self):
        return self._medal_flag

    @medal_flag.setter
    def medal_flag(self, value):
        self._medal_flag = value
    @property
    def schedule_status(self):
        return self._schedule_status

    @schedule_status.setter
    def schedule_status(self, value):
        self._schedule_status = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value
    @property
    def unit_code(self):
        return self._unit_code

    @unit_code.setter
    def unit_code(self, value):
        self._unit_code = value
    @property
    def venue_code(self):
        return self._venue_code

    @venue_code.setter
    def venue_code(self, value):
        self._venue_code = value
    @property
    def venue_name(self):
        return self._venue_name

    @venue_name.setter
    def venue_name(self, value):
        self._venue_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.actual_end_date:
            if hasattr(self.actual_end_date, 'to_alipay_dict'):
                params['actual_end_date'] = self.actual_end_date.to_alipay_dict()
            else:
                params['actual_end_date'] = self.actual_end_date
        if self.actual_start_date:
            if hasattr(self.actual_start_date, 'to_alipay_dict'):
                params['actual_start_date'] = self.actual_start_date.to_alipay_dict()
            else:
                params['actual_start_date'] = self.actual_start_date
        if self.cn_name:
            if hasattr(self.cn_name, 'to_alipay_dict'):
                params['cn_name'] = self.cn_name.to_alipay_dict()
            else:
                params['cn_name'] = self.cn_name
        if self.competition_code:
            if hasattr(self.competition_code, 'to_alipay_dict'):
                params['competition_code'] = self.competition_code.to_alipay_dict()
            else:
                params['competition_code'] = self.competition_code
        if self.data_version:
            if hasattr(self.data_version, 'to_alipay_dict'):
                params['data_version'] = self.data_version.to_alipay_dict()
            else:
                params['data_version'] = self.data_version
        if self.discipline:
            if hasattr(self.discipline, 'to_alipay_dict'):
                params['discipline'] = self.discipline.to_alipay_dict()
            else:
                params['discipline'] = self.discipline
        if self.en_name:
            if hasattr(self.en_name, 'to_alipay_dict'):
                params['en_name'] = self.en_name.to_alipay_dict()
            else:
                params['en_name'] = self.en_name
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.event_unit_type:
            if hasattr(self.event_unit_type, 'to_alipay_dict'):
                params['event_unit_type'] = self.event_unit_type.to_alipay_dict()
            else:
                params['event_unit_type'] = self.event_unit_type
        if self.hot_label:
            if hasattr(self.hot_label, 'to_alipay_dict'):
                params['hot_label'] = self.hot_label.to_alipay_dict()
            else:
                params['hot_label'] = self.hot_label
        if self.hot_level:
            if hasattr(self.hot_level, 'to_alipay_dict'):
                params['hot_level'] = self.hot_level.to_alipay_dict()
            else:
                params['hot_level'] = self.hot_level
        if self.location_code:
            if hasattr(self.location_code, 'to_alipay_dict'):
                params['location_code'] = self.location_code.to_alipay_dict()
            else:
                params['location_code'] = self.location_code
        if self.location_name:
            if hasattr(self.location_name, 'to_alipay_dict'):
                params['location_name'] = self.location_name.to_alipay_dict()
            else:
                params['location_name'] = self.location_name
        if self.medal_flag:
            if hasattr(self.medal_flag, 'to_alipay_dict'):
                params['medal_flag'] = self.medal_flag.to_alipay_dict()
            else:
                params['medal_flag'] = self.medal_flag
        if self.schedule_status:
            if hasattr(self.schedule_status, 'to_alipay_dict'):
                params['schedule_status'] = self.schedule_status.to_alipay_dict()
            else:
                params['schedule_status'] = self.schedule_status
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        if self.unit_code:
            if hasattr(self.unit_code, 'to_alipay_dict'):
                params['unit_code'] = self.unit_code.to_alipay_dict()
            else:
                params['unit_code'] = self.unit_code
        if self.venue_code:
            if hasattr(self.venue_code, 'to_alipay_dict'):
                params['venue_code'] = self.venue_code.to_alipay_dict()
            else:
                params['venue_code'] = self.venue_code
        if self.venue_name:
            if hasattr(self.venue_name, 'to_alipay_dict'):
                params['venue_name'] = self.venue_name.to_alipay_dict()
            else:
                params['venue_name'] = self.venue_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceSportsCompetitionScheduleSyncModel()
        if 'actual_end_date' in d:
            o.actual_end_date = d['actual_end_date']
        if 'actual_start_date' in d:
            o.actual_start_date = d['actual_start_date']
        if 'cn_name' in d:
            o.cn_name = d['cn_name']
        if 'competition_code' in d:
            o.competition_code = d['competition_code']
        if 'data_version' in d:
            o.data_version = d['data_version']
        if 'discipline' in d:
            o.discipline = d['discipline']
        if 'en_name' in d:
            o.en_name = d['en_name']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'event_unit_type' in d:
            o.event_unit_type = d['event_unit_type']
        if 'hot_label' in d:
            o.hot_label = d['hot_label']
        if 'hot_level' in d:
            o.hot_level = d['hot_level']
        if 'location_code' in d:
            o.location_code = d['location_code']
        if 'location_name' in d:
            o.location_name = d['location_name']
        if 'medal_flag' in d:
            o.medal_flag = d['medal_flag']
        if 'schedule_status' in d:
            o.schedule_status = d['schedule_status']
        if 'start_date' in d:
            o.start_date = d['start_date']
        if 'unit_code' in d:
            o.unit_code = d['unit_code']
        if 'venue_code' in d:
            o.venue_code = d['venue_code']
        if 'venue_name' in d:
            o.venue_name = d['venue_name']
        return o


