#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceIotSdarttoolPrintSendModel(object):

    def __init__(self):
        self._ext_info = None
        self._outer_no = None
        self._print_content = None
        self._print_template = None
        self._sence = None
        self._sn = None
        self._supplier_id = None
        self._walk_paper = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def outer_no(self):
        return self._outer_no

    @outer_no.setter
    def outer_no(self, value):
        self._outer_no = value
    @property
    def print_content(self):
        return self._print_content

    @print_content.setter
    def print_content(self, value):
        self._print_content = value
    @property
    def print_template(self):
        return self._print_template

    @print_template.setter
    def print_template(self, value):
        self._print_template = value
    @property
    def sence(self):
        return self._sence

    @sence.setter
    def sence(self, value):
        self._sence = value
    @property
    def sn(self):
        return self._sn

    @sn.setter
    def sn(self, value):
        self._sn = value
    @property
    def supplier_id(self):
        return self._supplier_id

    @supplier_id.setter
    def supplier_id(self, value):
        self._supplier_id = value
    @property
    def walk_paper(self):
        return self._walk_paper

    @walk_paper.setter
    def walk_paper(self, value):
        self._walk_paper = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.outer_no:
            if hasattr(self.outer_no, 'to_alipay_dict'):
                params['outer_no'] = self.outer_no.to_alipay_dict()
            else:
                params['outer_no'] = self.outer_no
        if self.print_content:
            if hasattr(self.print_content, 'to_alipay_dict'):
                params['print_content'] = self.print_content.to_alipay_dict()
            else:
                params['print_content'] = self.print_content
        if self.print_template:
            if hasattr(self.print_template, 'to_alipay_dict'):
                params['print_template'] = self.print_template.to_alipay_dict()
            else:
                params['print_template'] = self.print_template
        if self.sence:
            if hasattr(self.sence, 'to_alipay_dict'):
                params['sence'] = self.sence.to_alipay_dict()
            else:
                params['sence'] = self.sence
        if self.sn:
            if hasattr(self.sn, 'to_alipay_dict'):
                params['sn'] = self.sn.to_alipay_dict()
            else:
                params['sn'] = self.sn
        if self.supplier_id:
            if hasattr(self.supplier_id, 'to_alipay_dict'):
                params['supplier_id'] = self.supplier_id.to_alipay_dict()
            else:
                params['supplier_id'] = self.supplier_id
        if self.walk_paper:
            if hasattr(self.walk_paper, 'to_alipay_dict'):
                params['walk_paper'] = self.walk_paper.to_alipay_dict()
            else:
                params['walk_paper'] = self.walk_paper
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceIotSdarttoolPrintSendModel()
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'outer_no' in d:
            o.outer_no = d['outer_no']
        if 'print_content' in d:
            o.print_content = d['print_content']
        if 'print_template' in d:
            o.print_template = d['print_template']
        if 'sence' in d:
            o.sence = d['sence']
        if 'sn' in d:
            o.sn = d['sn']
        if 'supplier_id' in d:
            o.supplier_id = d['supplier_id']
        if 'walk_paper' in d:
            o.walk_paper = d['walk_paper']
        return o


