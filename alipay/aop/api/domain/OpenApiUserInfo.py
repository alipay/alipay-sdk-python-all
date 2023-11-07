#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenApiOrganizationNodeInfo import OpenApiOrganizationNodeInfo
from alipay.aop.api.domain.OpenApiRoleInfo import OpenApiRoleInfo
from alipay.aop.api.domain.OpenApiSkillGroupInfo import OpenApiSkillGroupInfo
from alipay.aop.api.domain.OpenApiUserResourceInfo import OpenApiUserResourceInfo
from alipay.aop.api.domain.OpenApiUserServeInfo import OpenApiUserServeInfo


class OpenApiUserInfo(object):

    def __init__(self):
        self._clv_user_id = None
        self._employee_code = None
        self._nick_name = None
        self._org_nodes = None
        self._risk_level = None
        self._roles = None
        self._skill_groups = None
        self._tnt_tnst_id = None
        self._user_id = None
        self._user_resource_info = None
        self._user_serve_info = None
        self._work_status = None

    @property
    def clv_user_id(self):
        return self._clv_user_id

    @clv_user_id.setter
    def clv_user_id(self, value):
        self._clv_user_id = value
    @property
    def employee_code(self):
        return self._employee_code

    @employee_code.setter
    def employee_code(self, value):
        self._employee_code = value
    @property
    def nick_name(self):
        return self._nick_name

    @nick_name.setter
    def nick_name(self, value):
        self._nick_name = value
    @property
    def org_nodes(self):
        return self._org_nodes

    @org_nodes.setter
    def org_nodes(self, value):
        if isinstance(value, list):
            self._org_nodes = list()
            for i in value:
                if isinstance(i, OpenApiOrganizationNodeInfo):
                    self._org_nodes.append(i)
                else:
                    self._org_nodes.append(OpenApiOrganizationNodeInfo.from_alipay_dict(i))
    @property
    def risk_level(self):
        return self._risk_level

    @risk_level.setter
    def risk_level(self, value):
        self._risk_level = value
    @property
    def roles(self):
        return self._roles

    @roles.setter
    def roles(self, value):
        if isinstance(value, list):
            self._roles = list()
            for i in value:
                if isinstance(i, OpenApiRoleInfo):
                    self._roles.append(i)
                else:
                    self._roles.append(OpenApiRoleInfo.from_alipay_dict(i))
    @property
    def skill_groups(self):
        return self._skill_groups

    @skill_groups.setter
    def skill_groups(self, value):
        if isinstance(value, list):
            self._skill_groups = list()
            for i in value:
                if isinstance(i, OpenApiSkillGroupInfo):
                    self._skill_groups.append(i)
                else:
                    self._skill_groups.append(OpenApiSkillGroupInfo.from_alipay_dict(i))
    @property
    def tnt_tnst_id(self):
        return self._tnt_tnst_id

    @tnt_tnst_id.setter
    def tnt_tnst_id(self, value):
        self._tnt_tnst_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_resource_info(self):
        return self._user_resource_info

    @user_resource_info.setter
    def user_resource_info(self, value):
        if isinstance(value, OpenApiUserResourceInfo):
            self._user_resource_info = value
        else:
            self._user_resource_info = OpenApiUserResourceInfo.from_alipay_dict(value)
    @property
    def user_serve_info(self):
        return self._user_serve_info

    @user_serve_info.setter
    def user_serve_info(self, value):
        if isinstance(value, OpenApiUserServeInfo):
            self._user_serve_info = value
        else:
            self._user_serve_info = OpenApiUserServeInfo.from_alipay_dict(value)
    @property
    def work_status(self):
        return self._work_status

    @work_status.setter
    def work_status(self, value):
        self._work_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.clv_user_id:
            if hasattr(self.clv_user_id, 'to_alipay_dict'):
                params['clv_user_id'] = self.clv_user_id.to_alipay_dict()
            else:
                params['clv_user_id'] = self.clv_user_id
        if self.employee_code:
            if hasattr(self.employee_code, 'to_alipay_dict'):
                params['employee_code'] = self.employee_code.to_alipay_dict()
            else:
                params['employee_code'] = self.employee_code
        if self.nick_name:
            if hasattr(self.nick_name, 'to_alipay_dict'):
                params['nick_name'] = self.nick_name.to_alipay_dict()
            else:
                params['nick_name'] = self.nick_name
        if self.org_nodes:
            if isinstance(self.org_nodes, list):
                for i in range(0, len(self.org_nodes)):
                    element = self.org_nodes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.org_nodes[i] = element.to_alipay_dict()
            if hasattr(self.org_nodes, 'to_alipay_dict'):
                params['org_nodes'] = self.org_nodes.to_alipay_dict()
            else:
                params['org_nodes'] = self.org_nodes
        if self.risk_level:
            if hasattr(self.risk_level, 'to_alipay_dict'):
                params['risk_level'] = self.risk_level.to_alipay_dict()
            else:
                params['risk_level'] = self.risk_level
        if self.roles:
            if isinstance(self.roles, list):
                for i in range(0, len(self.roles)):
                    element = self.roles[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.roles[i] = element.to_alipay_dict()
            if hasattr(self.roles, 'to_alipay_dict'):
                params['roles'] = self.roles.to_alipay_dict()
            else:
                params['roles'] = self.roles
        if self.skill_groups:
            if isinstance(self.skill_groups, list):
                for i in range(0, len(self.skill_groups)):
                    element = self.skill_groups[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.skill_groups[i] = element.to_alipay_dict()
            if hasattr(self.skill_groups, 'to_alipay_dict'):
                params['skill_groups'] = self.skill_groups.to_alipay_dict()
            else:
                params['skill_groups'] = self.skill_groups
        if self.tnt_tnst_id:
            if hasattr(self.tnt_tnst_id, 'to_alipay_dict'):
                params['tnt_tnst_id'] = self.tnt_tnst_id.to_alipay_dict()
            else:
                params['tnt_tnst_id'] = self.tnt_tnst_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_resource_info:
            if hasattr(self.user_resource_info, 'to_alipay_dict'):
                params['user_resource_info'] = self.user_resource_info.to_alipay_dict()
            else:
                params['user_resource_info'] = self.user_resource_info
        if self.user_serve_info:
            if hasattr(self.user_serve_info, 'to_alipay_dict'):
                params['user_serve_info'] = self.user_serve_info.to_alipay_dict()
            else:
                params['user_serve_info'] = self.user_serve_info
        if self.work_status:
            if hasattr(self.work_status, 'to_alipay_dict'):
                params['work_status'] = self.work_status.to_alipay_dict()
            else:
                params['work_status'] = self.work_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenApiUserInfo()
        if 'clv_user_id' in d:
            o.clv_user_id = d['clv_user_id']
        if 'employee_code' in d:
            o.employee_code = d['employee_code']
        if 'nick_name' in d:
            o.nick_name = d['nick_name']
        if 'org_nodes' in d:
            o.org_nodes = d['org_nodes']
        if 'risk_level' in d:
            o.risk_level = d['risk_level']
        if 'roles' in d:
            o.roles = d['roles']
        if 'skill_groups' in d:
            o.skill_groups = d['skill_groups']
        if 'tnt_tnst_id' in d:
            o.tnt_tnst_id = d['tnt_tnst_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_resource_info' in d:
            o.user_resource_info = d['user_resource_info']
        if 'user_serve_info' in d:
            o.user_serve_info = d['user_serve_info']
        if 'work_status' in d:
            o.work_status = d['work_status']
        return o


