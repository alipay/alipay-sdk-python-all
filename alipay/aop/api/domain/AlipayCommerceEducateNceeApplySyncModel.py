#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateNceeApplySyncModel(object):

    def __init__(self):
        self._batch = None
        self._course = None
        self._interested_major_num = None
        self._interested_school_num = None
        self._one_key_support = None
        self._province_code = None
        self._purpose_form_num = None
        self._rank = None
        self._report_num = None
        self._score = None
        self._selected_num = None
        self._subject = None
        self._total_num = None
        self._type = None
        self._user_id = None
        self._year = None

    @property
    def batch(self):
        return self._batch

    @batch.setter
    def batch(self, value):
        self._batch = value
    @property
    def course(self):
        return self._course

    @course.setter
    def course(self, value):
        self._course = value
    @property
    def interested_major_num(self):
        return self._interested_major_num

    @interested_major_num.setter
    def interested_major_num(self, value):
        self._interested_major_num = value
    @property
    def interested_school_num(self):
        return self._interested_school_num

    @interested_school_num.setter
    def interested_school_num(self, value):
        self._interested_school_num = value
    @property
    def one_key_support(self):
        return self._one_key_support

    @one_key_support.setter
    def one_key_support(self, value):
        self._one_key_support = value
    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value
    @property
    def purpose_form_num(self):
        return self._purpose_form_num

    @purpose_form_num.setter
    def purpose_form_num(self, value):
        self._purpose_form_num = value
    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, value):
        self._rank = value
    @property
    def report_num(self):
        return self._report_num

    @report_num.setter
    def report_num(self, value):
        self._report_num = value
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value
    @property
    def selected_num(self):
        return self._selected_num

    @selected_num.setter
    def selected_num(self, value):
        self._selected_num = value
    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value
    @property
    def total_num(self):
        return self._total_num

    @total_num.setter
    def total_num(self, value):
        self._total_num = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value


    def to_alipay_dict(self):
        params = dict()
        if self.batch:
            if hasattr(self.batch, 'to_alipay_dict'):
                params['batch'] = self.batch.to_alipay_dict()
            else:
                params['batch'] = self.batch
        if self.course:
            if hasattr(self.course, 'to_alipay_dict'):
                params['course'] = self.course.to_alipay_dict()
            else:
                params['course'] = self.course
        if self.interested_major_num:
            if hasattr(self.interested_major_num, 'to_alipay_dict'):
                params['interested_major_num'] = self.interested_major_num.to_alipay_dict()
            else:
                params['interested_major_num'] = self.interested_major_num
        if self.interested_school_num:
            if hasattr(self.interested_school_num, 'to_alipay_dict'):
                params['interested_school_num'] = self.interested_school_num.to_alipay_dict()
            else:
                params['interested_school_num'] = self.interested_school_num
        if self.one_key_support:
            if hasattr(self.one_key_support, 'to_alipay_dict'):
                params['one_key_support'] = self.one_key_support.to_alipay_dict()
            else:
                params['one_key_support'] = self.one_key_support
        if self.province_code:
            if hasattr(self.province_code, 'to_alipay_dict'):
                params['province_code'] = self.province_code.to_alipay_dict()
            else:
                params['province_code'] = self.province_code
        if self.purpose_form_num:
            if hasattr(self.purpose_form_num, 'to_alipay_dict'):
                params['purpose_form_num'] = self.purpose_form_num.to_alipay_dict()
            else:
                params['purpose_form_num'] = self.purpose_form_num
        if self.rank:
            if hasattr(self.rank, 'to_alipay_dict'):
                params['rank'] = self.rank.to_alipay_dict()
            else:
                params['rank'] = self.rank
        if self.report_num:
            if hasattr(self.report_num, 'to_alipay_dict'):
                params['report_num'] = self.report_num.to_alipay_dict()
            else:
                params['report_num'] = self.report_num
        if self.score:
            if hasattr(self.score, 'to_alipay_dict'):
                params['score'] = self.score.to_alipay_dict()
            else:
                params['score'] = self.score
        if self.selected_num:
            if hasattr(self.selected_num, 'to_alipay_dict'):
                params['selected_num'] = self.selected_num.to_alipay_dict()
            else:
                params['selected_num'] = self.selected_num
        if self.subject:
            if hasattr(self.subject, 'to_alipay_dict'):
                params['subject'] = self.subject.to_alipay_dict()
            else:
                params['subject'] = self.subject
        if self.total_num:
            if hasattr(self.total_num, 'to_alipay_dict'):
                params['total_num'] = self.total_num.to_alipay_dict()
            else:
                params['total_num'] = self.total_num
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.year:
            if hasattr(self.year, 'to_alipay_dict'):
                params['year'] = self.year.to_alipay_dict()
            else:
                params['year'] = self.year
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateNceeApplySyncModel()
        if 'batch' in d:
            o.batch = d['batch']
        if 'course' in d:
            o.course = d['course']
        if 'interested_major_num' in d:
            o.interested_major_num = d['interested_major_num']
        if 'interested_school_num' in d:
            o.interested_school_num = d['interested_school_num']
        if 'one_key_support' in d:
            o.one_key_support = d['one_key_support']
        if 'province_code' in d:
            o.province_code = d['province_code']
        if 'purpose_form_num' in d:
            o.purpose_form_num = d['purpose_form_num']
        if 'rank' in d:
            o.rank = d['rank']
        if 'report_num' in d:
            o.report_num = d['report_num']
        if 'score' in d:
            o.score = d['score']
        if 'selected_num' in d:
            o.selected_num = d['selected_num']
        if 'subject' in d:
            o.subject = d['subject']
        if 'total_num' in d:
            o.total_num = d['total_num']
        if 'type' in d:
            o.type = d['type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'year' in d:
            o.year = d['year']
        return o


