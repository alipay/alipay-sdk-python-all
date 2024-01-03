#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IcpAuditInfoList import IcpAuditInfoList


class IcpAppletsInfo(object):

    def __init__(self):
        self._attachement_materials = None
        self._comment = None
        self._icp_audit_infos = None
        self._main_category_id = None

    @property
    def attachement_materials(self):
        return self._attachement_materials

    @attachement_materials.setter
    def attachement_materials(self, value):
        if isinstance(value, list):
            self._attachement_materials = list()
            for i in value:
                self._attachement_materials.append(i)
    @property
    def comment(self):
        return self._comment

    @comment.setter
    def comment(self, value):
        self._comment = value
    @property
    def icp_audit_infos(self):
        return self._icp_audit_infos

    @icp_audit_infos.setter
    def icp_audit_infos(self, value):
        if isinstance(value, list):
            self._icp_audit_infos = list()
            for i in value:
                if isinstance(i, IcpAuditInfoList):
                    self._icp_audit_infos.append(i)
                else:
                    self._icp_audit_infos.append(IcpAuditInfoList.from_alipay_dict(i))
    @property
    def main_category_id(self):
        return self._main_category_id

    @main_category_id.setter
    def main_category_id(self, value):
        self._main_category_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.attachement_materials:
            if isinstance(self.attachement_materials, list):
                for i in range(0, len(self.attachement_materials)):
                    element = self.attachement_materials[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.attachement_materials[i] = element.to_alipay_dict()
            if hasattr(self.attachement_materials, 'to_alipay_dict'):
                params['attachement_materials'] = self.attachement_materials.to_alipay_dict()
            else:
                params['attachement_materials'] = self.attachement_materials
        if self.comment:
            if hasattr(self.comment, 'to_alipay_dict'):
                params['comment'] = self.comment.to_alipay_dict()
            else:
                params['comment'] = self.comment
        if self.icp_audit_infos:
            if isinstance(self.icp_audit_infos, list):
                for i in range(0, len(self.icp_audit_infos)):
                    element = self.icp_audit_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.icp_audit_infos[i] = element.to_alipay_dict()
            if hasattr(self.icp_audit_infos, 'to_alipay_dict'):
                params['icp_audit_infos'] = self.icp_audit_infos.to_alipay_dict()
            else:
                params['icp_audit_infos'] = self.icp_audit_infos
        if self.main_category_id:
            if hasattr(self.main_category_id, 'to_alipay_dict'):
                params['main_category_id'] = self.main_category_id.to_alipay_dict()
            else:
                params['main_category_id'] = self.main_category_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IcpAppletsInfo()
        if 'attachement_materials' in d:
            o.attachement_materials = d['attachement_materials']
        if 'comment' in d:
            o.comment = d['comment']
        if 'icp_audit_infos' in d:
            o.icp_audit_infos = d['icp_audit_infos']
        if 'main_category_id' in d:
            o.main_category_id = d['main_category_id']
        return o


