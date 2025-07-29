#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceFhyeduRollcallSyncModel(object):

    def __init__(self):
        self._attended_status = None
        self._begin_time = None
        self._class_name = None
        self._class_room_name = None
        self._consumed_quantity = None
        self._consumed_unit = None
        self._consumption_target_id = None
        self._consumption_target_name = None
        self._consumption_way = None
        self._content = None
        self._course_id = None
        self._course_name = None
        self._end_time = None
        self._inst_id = None
        self._memo = None
        self._over_quantity = None
        self._over_scheduled = None
        self._over_unit = None
        self._roll_call_id = None
        self._roll_call_time = None
        self._sched_id = None
        self._student_id = None
        self._teacher_name = None

    @property
    def attended_status(self):
        return self._attended_status

    @attended_status.setter
    def attended_status(self, value):
        self._attended_status = value
    @property
    def begin_time(self):
        return self._begin_time

    @begin_time.setter
    def begin_time(self, value):
        self._begin_time = value
    @property
    def class_name(self):
        return self._class_name

    @class_name.setter
    def class_name(self, value):
        self._class_name = value
    @property
    def class_room_name(self):
        return self._class_room_name

    @class_room_name.setter
    def class_room_name(self, value):
        self._class_room_name = value
    @property
    def consumed_quantity(self):
        return self._consumed_quantity

    @consumed_quantity.setter
    def consumed_quantity(self, value):
        self._consumed_quantity = value
    @property
    def consumed_unit(self):
        return self._consumed_unit

    @consumed_unit.setter
    def consumed_unit(self, value):
        self._consumed_unit = value
    @property
    def consumption_target_id(self):
        return self._consumption_target_id

    @consumption_target_id.setter
    def consumption_target_id(self, value):
        self._consumption_target_id = value
    @property
    def consumption_target_name(self):
        return self._consumption_target_name

    @consumption_target_name.setter
    def consumption_target_name(self, value):
        self._consumption_target_name = value
    @property
    def consumption_way(self):
        return self._consumption_way

    @consumption_way.setter
    def consumption_way(self, value):
        self._consumption_way = value
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def course_id(self):
        return self._course_id

    @course_id.setter
    def course_id(self, value):
        self._course_id = value
    @property
    def course_name(self):
        return self._course_name

    @course_name.setter
    def course_name(self, value):
        self._course_name = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def over_quantity(self):
        return self._over_quantity

    @over_quantity.setter
    def over_quantity(self, value):
        self._over_quantity = value
    @property
    def over_scheduled(self):
        return self._over_scheduled

    @over_scheduled.setter
    def over_scheduled(self, value):
        self._over_scheduled = value
    @property
    def over_unit(self):
        return self._over_unit

    @over_unit.setter
    def over_unit(self, value):
        self._over_unit = value
    @property
    def roll_call_id(self):
        return self._roll_call_id

    @roll_call_id.setter
    def roll_call_id(self, value):
        self._roll_call_id = value
    @property
    def roll_call_time(self):
        return self._roll_call_time

    @roll_call_time.setter
    def roll_call_time(self, value):
        self._roll_call_time = value
    @property
    def sched_id(self):
        return self._sched_id

    @sched_id.setter
    def sched_id(self, value):
        self._sched_id = value
    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, value):
        self._student_id = value
    @property
    def teacher_name(self):
        return self._teacher_name

    @teacher_name.setter
    def teacher_name(self, value):
        self._teacher_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.attended_status:
            if hasattr(self.attended_status, 'to_alipay_dict'):
                params['attended_status'] = self.attended_status.to_alipay_dict()
            else:
                params['attended_status'] = self.attended_status
        if self.begin_time:
            if hasattr(self.begin_time, 'to_alipay_dict'):
                params['begin_time'] = self.begin_time.to_alipay_dict()
            else:
                params['begin_time'] = self.begin_time
        if self.class_name:
            if hasattr(self.class_name, 'to_alipay_dict'):
                params['class_name'] = self.class_name.to_alipay_dict()
            else:
                params['class_name'] = self.class_name
        if self.class_room_name:
            if hasattr(self.class_room_name, 'to_alipay_dict'):
                params['class_room_name'] = self.class_room_name.to_alipay_dict()
            else:
                params['class_room_name'] = self.class_room_name
        if self.consumed_quantity:
            if hasattr(self.consumed_quantity, 'to_alipay_dict'):
                params['consumed_quantity'] = self.consumed_quantity.to_alipay_dict()
            else:
                params['consumed_quantity'] = self.consumed_quantity
        if self.consumed_unit:
            if hasattr(self.consumed_unit, 'to_alipay_dict'):
                params['consumed_unit'] = self.consumed_unit.to_alipay_dict()
            else:
                params['consumed_unit'] = self.consumed_unit
        if self.consumption_target_id:
            if hasattr(self.consumption_target_id, 'to_alipay_dict'):
                params['consumption_target_id'] = self.consumption_target_id.to_alipay_dict()
            else:
                params['consumption_target_id'] = self.consumption_target_id
        if self.consumption_target_name:
            if hasattr(self.consumption_target_name, 'to_alipay_dict'):
                params['consumption_target_name'] = self.consumption_target_name.to_alipay_dict()
            else:
                params['consumption_target_name'] = self.consumption_target_name
        if self.consumption_way:
            if hasattr(self.consumption_way, 'to_alipay_dict'):
                params['consumption_way'] = self.consumption_way.to_alipay_dict()
            else:
                params['consumption_way'] = self.consumption_way
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.course_id:
            if hasattr(self.course_id, 'to_alipay_dict'):
                params['course_id'] = self.course_id.to_alipay_dict()
            else:
                params['course_id'] = self.course_id
        if self.course_name:
            if hasattr(self.course_name, 'to_alipay_dict'):
                params['course_name'] = self.course_name.to_alipay_dict()
            else:
                params['course_name'] = self.course_name
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.over_quantity:
            if hasattr(self.over_quantity, 'to_alipay_dict'):
                params['over_quantity'] = self.over_quantity.to_alipay_dict()
            else:
                params['over_quantity'] = self.over_quantity
        if self.over_scheduled:
            if hasattr(self.over_scheduled, 'to_alipay_dict'):
                params['over_scheduled'] = self.over_scheduled.to_alipay_dict()
            else:
                params['over_scheduled'] = self.over_scheduled
        if self.over_unit:
            if hasattr(self.over_unit, 'to_alipay_dict'):
                params['over_unit'] = self.over_unit.to_alipay_dict()
            else:
                params['over_unit'] = self.over_unit
        if self.roll_call_id:
            if hasattr(self.roll_call_id, 'to_alipay_dict'):
                params['roll_call_id'] = self.roll_call_id.to_alipay_dict()
            else:
                params['roll_call_id'] = self.roll_call_id
        if self.roll_call_time:
            if hasattr(self.roll_call_time, 'to_alipay_dict'):
                params['roll_call_time'] = self.roll_call_time.to_alipay_dict()
            else:
                params['roll_call_time'] = self.roll_call_time
        if self.sched_id:
            if hasattr(self.sched_id, 'to_alipay_dict'):
                params['sched_id'] = self.sched_id.to_alipay_dict()
            else:
                params['sched_id'] = self.sched_id
        if self.student_id:
            if hasattr(self.student_id, 'to_alipay_dict'):
                params['student_id'] = self.student_id.to_alipay_dict()
            else:
                params['student_id'] = self.student_id
        if self.teacher_name:
            if hasattr(self.teacher_name, 'to_alipay_dict'):
                params['teacher_name'] = self.teacher_name.to_alipay_dict()
            else:
                params['teacher_name'] = self.teacher_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceFhyeduRollcallSyncModel()
        if 'attended_status' in d:
            o.attended_status = d['attended_status']
        if 'begin_time' in d:
            o.begin_time = d['begin_time']
        if 'class_name' in d:
            o.class_name = d['class_name']
        if 'class_room_name' in d:
            o.class_room_name = d['class_room_name']
        if 'consumed_quantity' in d:
            o.consumed_quantity = d['consumed_quantity']
        if 'consumed_unit' in d:
            o.consumed_unit = d['consumed_unit']
        if 'consumption_target_id' in d:
            o.consumption_target_id = d['consumption_target_id']
        if 'consumption_target_name' in d:
            o.consumption_target_name = d['consumption_target_name']
        if 'consumption_way' in d:
            o.consumption_way = d['consumption_way']
        if 'content' in d:
            o.content = d['content']
        if 'course_id' in d:
            o.course_id = d['course_id']
        if 'course_name' in d:
            o.course_name = d['course_name']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'memo' in d:
            o.memo = d['memo']
        if 'over_quantity' in d:
            o.over_quantity = d['over_quantity']
        if 'over_scheduled' in d:
            o.over_scheduled = d['over_scheduled']
        if 'over_unit' in d:
            o.over_unit = d['over_unit']
        if 'roll_call_id' in d:
            o.roll_call_id = d['roll_call_id']
        if 'roll_call_time' in d:
            o.roll_call_time = d['roll_call_time']
        if 'sched_id' in d:
            o.sched_id = d['sched_id']
        if 'student_id' in d:
            o.student_id = d['student_id']
        if 'teacher_name' in d:
            o.teacher_name = d['teacher_name']
        return o


