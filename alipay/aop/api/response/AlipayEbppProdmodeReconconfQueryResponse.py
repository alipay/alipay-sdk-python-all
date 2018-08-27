#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppProdmodeReconconfQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppProdmodeReconconfQueryResponse, self).__init__()
        self._check_depend = None
        self._check_grade = None
        self._clear_grade = None
        self._cut_hour = None
        self._cut_min = None
        self._cut_sec = None
        self._has_recon_conf = None
        self._no_conf_reason = None
        self._recon_time = None
        self._refund_rule = None

    @property
    def check_depend(self):
        return self._check_depend

    @check_depend.setter
    def check_depend(self, value):
        self._check_depend = value
    @property
    def check_grade(self):
        return self._check_grade

    @check_grade.setter
    def check_grade(self, value):
        self._check_grade = value
    @property
    def clear_grade(self):
        return self._clear_grade

    @clear_grade.setter
    def clear_grade(self, value):
        self._clear_grade = value
    @property
    def cut_hour(self):
        return self._cut_hour

    @cut_hour.setter
    def cut_hour(self, value):
        self._cut_hour = value
    @property
    def cut_min(self):
        return self._cut_min

    @cut_min.setter
    def cut_min(self, value):
        self._cut_min = value
    @property
    def cut_sec(self):
        return self._cut_sec

    @cut_sec.setter
    def cut_sec(self, value):
        self._cut_sec = value
    @property
    def has_recon_conf(self):
        return self._has_recon_conf

    @has_recon_conf.setter
    def has_recon_conf(self, value):
        self._has_recon_conf = value
    @property
    def no_conf_reason(self):
        return self._no_conf_reason

    @no_conf_reason.setter
    def no_conf_reason(self, value):
        self._no_conf_reason = value
    @property
    def recon_time(self):
        return self._recon_time

    @recon_time.setter
    def recon_time(self, value):
        self._recon_time = value
    @property
    def refund_rule(self):
        return self._refund_rule

    @refund_rule.setter
    def refund_rule(self, value):
        self._refund_rule = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppProdmodeReconconfQueryResponse, self).parse_response_content(response_content)
        if 'check_depend' in response:
            self.check_depend = response['check_depend']
        if 'check_grade' in response:
            self.check_grade = response['check_grade']
        if 'clear_grade' in response:
            self.clear_grade = response['clear_grade']
        if 'cut_hour' in response:
            self.cut_hour = response['cut_hour']
        if 'cut_min' in response:
            self.cut_min = response['cut_min']
        if 'cut_sec' in response:
            self.cut_sec = response['cut_sec']
        if 'has_recon_conf' in response:
            self.has_recon_conf = response['has_recon_conf']
        if 'no_conf_reason' in response:
            self.no_conf_reason = response['no_conf_reason']
        if 'recon_time' in response:
            self.recon_time = response['recon_time']
        if 'refund_rule' in response:
            self.refund_rule = response['refund_rule']
