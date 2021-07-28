#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CreditBankCredit(object):

    def __init__(self):
        self._course_name = None
        self._course_property = None
        self._course_result_code = None
        self._course_score = None
        self._course_season = None
        self._course_subject = None
        self._course_year = None
        self._credit = None
        self._credit_hour = None
        self._credit_outer_id = None
        self._experience_time = None
        self._inst_name = None
        self._learning_stage = None

    @property
    def course_name(self):
        return self._course_name

    @course_name.setter
    def course_name(self, value):
        self._course_name = value
    @property
    def course_property(self):
        return self._course_property

    @course_property.setter
    def course_property(self, value):
        self._course_property = value
    @property
    def course_result_code(self):
        return self._course_result_code

    @course_result_code.setter
    def course_result_code(self, value):
        self._course_result_code = value
    @property
    def course_score(self):
        return self._course_score

    @course_score.setter
    def course_score(self, value):
        self._course_score = value
    @property
    def course_season(self):
        return self._course_season

    @course_season.setter
    def course_season(self, value):
        self._course_season = value
    @property
    def course_subject(self):
        return self._course_subject

    @course_subject.setter
    def course_subject(self, value):
        self._course_subject = value
    @property
    def course_year(self):
        return self._course_year

    @course_year.setter
    def course_year(self, value):
        self._course_year = value
    @property
    def credit(self):
        return self._credit

    @credit.setter
    def credit(self, value):
        self._credit = value
    @property
    def credit_hour(self):
        return self._credit_hour

    @credit_hour.setter
    def credit_hour(self, value):
        self._credit_hour = value
    @property
    def credit_outer_id(self):
        return self._credit_outer_id

    @credit_outer_id.setter
    def credit_outer_id(self, value):
        self._credit_outer_id = value
    @property
    def experience_time(self):
        return self._experience_time

    @experience_time.setter
    def experience_time(self, value):
        self._experience_time = value
    @property
    def inst_name(self):
        return self._inst_name

    @inst_name.setter
    def inst_name(self, value):
        self._inst_name = value
    @property
    def learning_stage(self):
        return self._learning_stage

    @learning_stage.setter
    def learning_stage(self, value):
        self._learning_stage = value


    def to_alipay_dict(self):
        params = dict()
        if self.course_name:
            if hasattr(self.course_name, 'to_alipay_dict'):
                params['course_name'] = self.course_name.to_alipay_dict()
            else:
                params['course_name'] = self.course_name
        if self.course_property:
            if hasattr(self.course_property, 'to_alipay_dict'):
                params['course_property'] = self.course_property.to_alipay_dict()
            else:
                params['course_property'] = self.course_property
        if self.course_result_code:
            if hasattr(self.course_result_code, 'to_alipay_dict'):
                params['course_result_code'] = self.course_result_code.to_alipay_dict()
            else:
                params['course_result_code'] = self.course_result_code
        if self.course_score:
            if hasattr(self.course_score, 'to_alipay_dict'):
                params['course_score'] = self.course_score.to_alipay_dict()
            else:
                params['course_score'] = self.course_score
        if self.course_season:
            if hasattr(self.course_season, 'to_alipay_dict'):
                params['course_season'] = self.course_season.to_alipay_dict()
            else:
                params['course_season'] = self.course_season
        if self.course_subject:
            if hasattr(self.course_subject, 'to_alipay_dict'):
                params['course_subject'] = self.course_subject.to_alipay_dict()
            else:
                params['course_subject'] = self.course_subject
        if self.course_year:
            if hasattr(self.course_year, 'to_alipay_dict'):
                params['course_year'] = self.course_year.to_alipay_dict()
            else:
                params['course_year'] = self.course_year
        if self.credit:
            if hasattr(self.credit, 'to_alipay_dict'):
                params['credit'] = self.credit.to_alipay_dict()
            else:
                params['credit'] = self.credit
        if self.credit_hour:
            if hasattr(self.credit_hour, 'to_alipay_dict'):
                params['credit_hour'] = self.credit_hour.to_alipay_dict()
            else:
                params['credit_hour'] = self.credit_hour
        if self.credit_outer_id:
            if hasattr(self.credit_outer_id, 'to_alipay_dict'):
                params['credit_outer_id'] = self.credit_outer_id.to_alipay_dict()
            else:
                params['credit_outer_id'] = self.credit_outer_id
        if self.experience_time:
            if hasattr(self.experience_time, 'to_alipay_dict'):
                params['experience_time'] = self.experience_time.to_alipay_dict()
            else:
                params['experience_time'] = self.experience_time
        if self.inst_name:
            if hasattr(self.inst_name, 'to_alipay_dict'):
                params['inst_name'] = self.inst_name.to_alipay_dict()
            else:
                params['inst_name'] = self.inst_name
        if self.learning_stage:
            if hasattr(self.learning_stage, 'to_alipay_dict'):
                params['learning_stage'] = self.learning_stage.to_alipay_dict()
            else:
                params['learning_stage'] = self.learning_stage
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CreditBankCredit()
        if 'course_name' in d:
            o.course_name = d['course_name']
        if 'course_property' in d:
            o.course_property = d['course_property']
        if 'course_result_code' in d:
            o.course_result_code = d['course_result_code']
        if 'course_score' in d:
            o.course_score = d['course_score']
        if 'course_season' in d:
            o.course_season = d['course_season']
        if 'course_subject' in d:
            o.course_subject = d['course_subject']
        if 'course_year' in d:
            o.course_year = d['course_year']
        if 'credit' in d:
            o.credit = d['credit']
        if 'credit_hour' in d:
            o.credit_hour = d['credit_hour']
        if 'credit_outer_id' in d:
            o.credit_outer_id = d['credit_outer_id']
        if 'experience_time' in d:
            o.experience_time = d['experience_time']
        if 'inst_name' in d:
            o.inst_name = d['inst_name']
        if 'learning_stage' in d:
            o.learning_stage = d['learning_stage']
        return o


