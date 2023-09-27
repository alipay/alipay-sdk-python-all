#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ConfigOutDTO import ConfigOutDTO
from alipay.aop.api.domain.ContractOrderSendLogDTO import ContractOrderSendLogDTO
from alipay.aop.api.domain.DateRangeDTO import DateRangeDTO
from alipay.aop.api.domain.AecpFileDTO import AecpFileDTO
from alipay.aop.api.domain.PurchaseOrderItemOutDTO import PurchaseOrderItemOutDTO
from alipay.aop.api.domain.PaymentPlanDTO import PaymentPlanDTO
from alipay.aop.api.domain.PoBillableInfoDto import PoBillableInfoDto
from alipay.aop.api.domain.LinkDTO import LinkDTO


class PurchaseOrderOutDTO(object):

    def __init__(self):
        self._amount_visible = None
        self._antgroup_account = None
        self._bank_account = None
        self._bank_branch_name = None
        self._biz_type = None
        self._buyer = None
        self._buyer_dept_code = None
        self._buyer_manager = None
        self._buyer_purchase_org_id = None
        self._company_code = None
        self._company_name = None
        self._config_out_dto = None
        self._confirmed = None
        self._contract_number = None
        self._contract_order_send_log_dto_list = None
        self._contract_type = None
        self._creator = None
        self._currency = None
        self._data_source = None
        self._demander_purchase_org_id = None
        self._description = None
        self._effect_date_range = None
        self._effect_date_range_end = None
        self._effect_date_range_start = None
        self._effect_time = None
        self._email_status = None
        self._exchange_rate = None
        self._external_po_number = None
        self._file_list = None
        self._files = None
        self._gmt_create = None
        self._gmt_modified = None
        self._has_electronic_sign = None
        self._id = None
        self._invoiced_amount = None
        self._is_ant_group = None
        self._is_cash_pay = None
        self._is_cheque_pay = None
        self._is_delivery_detail = None
        self._is_expire_remind = None
        self._item_list = None
        self._modifier = None
        self._no_contract_reason = None
        self._order_channel = None
        self._origin_currency = None
        self._ou_code = None
        self._paid_amount = None
        self._payee_account_name = None
        self._payee_bank_id = None
        self._payee_id = None
        self._payee_name = None
        self._payment_plan_dto = None
        self._po_billable_info_dto = None
        self._po_number = None
        self._quotation_approved_time = None
        self._quotation_number = None
        self._reusable_contract_code = None
        self._source_type = None
        self._status = None
        self._structured_detail_biz_scene = None
        self._supplier_id = None
        self._supplier_link = None
        self._tenant_id = None
        self._to_paid_amount = None
        self._total_amount = None

    @property
    def amount_visible(self):
        return self._amount_visible

    @amount_visible.setter
    def amount_visible(self, value):
        self._amount_visible = value
    @property
    def antgroup_account(self):
        return self._antgroup_account

    @antgroup_account.setter
    def antgroup_account(self, value):
        self._antgroup_account = value
    @property
    def bank_account(self):
        return self._bank_account

    @bank_account.setter
    def bank_account(self, value):
        self._bank_account = value
    @property
    def bank_branch_name(self):
        return self._bank_branch_name

    @bank_branch_name.setter
    def bank_branch_name(self, value):
        self._bank_branch_name = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def buyer(self):
        return self._buyer

    @buyer.setter
    def buyer(self, value):
        self._buyer = value
    @property
    def buyer_dept_code(self):
        return self._buyer_dept_code

    @buyer_dept_code.setter
    def buyer_dept_code(self, value):
        self._buyer_dept_code = value
    @property
    def buyer_manager(self):
        return self._buyer_manager

    @buyer_manager.setter
    def buyer_manager(self, value):
        self._buyer_manager = value
    @property
    def buyer_purchase_org_id(self):
        return self._buyer_purchase_org_id

    @buyer_purchase_org_id.setter
    def buyer_purchase_org_id(self, value):
        self._buyer_purchase_org_id = value
    @property
    def company_code(self):
        return self._company_code

    @company_code.setter
    def company_code(self, value):
        self._company_code = value
    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        self._company_name = value
    @property
    def config_out_dto(self):
        return self._config_out_dto

    @config_out_dto.setter
    def config_out_dto(self, value):
        if isinstance(value, ConfigOutDTO):
            self._config_out_dto = value
        else:
            self._config_out_dto = ConfigOutDTO.from_alipay_dict(value)
    @property
    def confirmed(self):
        return self._confirmed

    @confirmed.setter
    def confirmed(self, value):
        self._confirmed = value
    @property
    def contract_number(self):
        return self._contract_number

    @contract_number.setter
    def contract_number(self, value):
        self._contract_number = value
    @property
    def contract_order_send_log_dto_list(self):
        return self._contract_order_send_log_dto_list

    @contract_order_send_log_dto_list.setter
    def contract_order_send_log_dto_list(self, value):
        if isinstance(value, list):
            self._contract_order_send_log_dto_list = list()
            for i in value:
                if isinstance(i, ContractOrderSendLogDTO):
                    self._contract_order_send_log_dto_list.append(i)
                else:
                    self._contract_order_send_log_dto_list.append(ContractOrderSendLogDTO.from_alipay_dict(i))
    @property
    def contract_type(self):
        return self._contract_type

    @contract_type.setter
    def contract_type(self, value):
        self._contract_type = value
    @property
    def creator(self):
        return self._creator

    @creator.setter
    def creator(self, value):
        self._creator = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def data_source(self):
        return self._data_source

    @data_source.setter
    def data_source(self, value):
        self._data_source = value
    @property
    def demander_purchase_org_id(self):
        return self._demander_purchase_org_id

    @demander_purchase_org_id.setter
    def demander_purchase_org_id(self, value):
        self._demander_purchase_org_id = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def effect_date_range(self):
        return self._effect_date_range

    @effect_date_range.setter
    def effect_date_range(self, value):
        if isinstance(value, DateRangeDTO):
            self._effect_date_range = value
        else:
            self._effect_date_range = DateRangeDTO.from_alipay_dict(value)
    @property
    def effect_date_range_end(self):
        return self._effect_date_range_end

    @effect_date_range_end.setter
    def effect_date_range_end(self, value):
        self._effect_date_range_end = value
    @property
    def effect_date_range_start(self):
        return self._effect_date_range_start

    @effect_date_range_start.setter
    def effect_date_range_start(self, value):
        self._effect_date_range_start = value
    @property
    def effect_time(self):
        return self._effect_time

    @effect_time.setter
    def effect_time(self, value):
        self._effect_time = value
    @property
    def email_status(self):
        return self._email_status

    @email_status.setter
    def email_status(self, value):
        self._email_status = value
    @property
    def exchange_rate(self):
        return self._exchange_rate

    @exchange_rate.setter
    def exchange_rate(self, value):
        self._exchange_rate = value
    @property
    def external_po_number(self):
        return self._external_po_number

    @external_po_number.setter
    def external_po_number(self, value):
        self._external_po_number = value
    @property
    def file_list(self):
        return self._file_list

    @file_list.setter
    def file_list(self, value):
        if isinstance(value, list):
            self._file_list = list()
            for i in value:
                if isinstance(i, AecpFileDTO):
                    self._file_list.append(i)
                else:
                    self._file_list.append(AecpFileDTO.from_alipay_dict(i))
    @property
    def files(self):
        return self._files

    @files.setter
    def files(self, value):
        self._files = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def has_electronic_sign(self):
        return self._has_electronic_sign

    @has_electronic_sign.setter
    def has_electronic_sign(self, value):
        self._has_electronic_sign = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def invoiced_amount(self):
        return self._invoiced_amount

    @invoiced_amount.setter
    def invoiced_amount(self, value):
        self._invoiced_amount = value
    @property
    def is_ant_group(self):
        return self._is_ant_group

    @is_ant_group.setter
    def is_ant_group(self, value):
        self._is_ant_group = value
    @property
    def is_cash_pay(self):
        return self._is_cash_pay

    @is_cash_pay.setter
    def is_cash_pay(self, value):
        self._is_cash_pay = value
    @property
    def is_cheque_pay(self):
        return self._is_cheque_pay

    @is_cheque_pay.setter
    def is_cheque_pay(self, value):
        self._is_cheque_pay = value
    @property
    def is_delivery_detail(self):
        return self._is_delivery_detail

    @is_delivery_detail.setter
    def is_delivery_detail(self, value):
        self._is_delivery_detail = value
    @property
    def is_expire_remind(self):
        return self._is_expire_remind

    @is_expire_remind.setter
    def is_expire_remind(self, value):
        self._is_expire_remind = value
    @property
    def item_list(self):
        return self._item_list

    @item_list.setter
    def item_list(self, value):
        if isinstance(value, list):
            self._item_list = list()
            for i in value:
                if isinstance(i, PurchaseOrderItemOutDTO):
                    self._item_list.append(i)
                else:
                    self._item_list.append(PurchaseOrderItemOutDTO.from_alipay_dict(i))
    @property
    def modifier(self):
        return self._modifier

    @modifier.setter
    def modifier(self, value):
        self._modifier = value
    @property
    def no_contract_reason(self):
        return self._no_contract_reason

    @no_contract_reason.setter
    def no_contract_reason(self, value):
        self._no_contract_reason = value
    @property
    def order_channel(self):
        return self._order_channel

    @order_channel.setter
    def order_channel(self, value):
        self._order_channel = value
    @property
    def origin_currency(self):
        return self._origin_currency

    @origin_currency.setter
    def origin_currency(self, value):
        self._origin_currency = value
    @property
    def ou_code(self):
        return self._ou_code

    @ou_code.setter
    def ou_code(self, value):
        self._ou_code = value
    @property
    def paid_amount(self):
        return self._paid_amount

    @paid_amount.setter
    def paid_amount(self, value):
        self._paid_amount = value
    @property
    def payee_account_name(self):
        return self._payee_account_name

    @payee_account_name.setter
    def payee_account_name(self, value):
        self._payee_account_name = value
    @property
    def payee_bank_id(self):
        return self._payee_bank_id

    @payee_bank_id.setter
    def payee_bank_id(self, value):
        self._payee_bank_id = value
    @property
    def payee_id(self):
        return self._payee_id

    @payee_id.setter
    def payee_id(self, value):
        self._payee_id = value
    @property
    def payee_name(self):
        return self._payee_name

    @payee_name.setter
    def payee_name(self, value):
        self._payee_name = value
    @property
    def payment_plan_dto(self):
        return self._payment_plan_dto

    @payment_plan_dto.setter
    def payment_plan_dto(self, value):
        if isinstance(value, PaymentPlanDTO):
            self._payment_plan_dto = value
        else:
            self._payment_plan_dto = PaymentPlanDTO.from_alipay_dict(value)
    @property
    def po_billable_info_dto(self):
        return self._po_billable_info_dto

    @po_billable_info_dto.setter
    def po_billable_info_dto(self, value):
        if isinstance(value, PoBillableInfoDto):
            self._po_billable_info_dto = value
        else:
            self._po_billable_info_dto = PoBillableInfoDto.from_alipay_dict(value)
    @property
    def po_number(self):
        return self._po_number

    @po_number.setter
    def po_number(self, value):
        self._po_number = value
    @property
    def quotation_approved_time(self):
        return self._quotation_approved_time

    @quotation_approved_time.setter
    def quotation_approved_time(self, value):
        self._quotation_approved_time = value
    @property
    def quotation_number(self):
        return self._quotation_number

    @quotation_number.setter
    def quotation_number(self, value):
        self._quotation_number = value
    @property
    def reusable_contract_code(self):
        return self._reusable_contract_code

    @reusable_contract_code.setter
    def reusable_contract_code(self, value):
        self._reusable_contract_code = value
    @property
    def source_type(self):
        return self._source_type

    @source_type.setter
    def source_type(self, value):
        self._source_type = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def structured_detail_biz_scene(self):
        return self._structured_detail_biz_scene

    @structured_detail_biz_scene.setter
    def structured_detail_biz_scene(self, value):
        self._structured_detail_biz_scene = value
    @property
    def supplier_id(self):
        return self._supplier_id

    @supplier_id.setter
    def supplier_id(self, value):
        self._supplier_id = value
    @property
    def supplier_link(self):
        return self._supplier_link

    @supplier_link.setter
    def supplier_link(self, value):
        if isinstance(value, LinkDTO):
            self._supplier_link = value
        else:
            self._supplier_link = LinkDTO.from_alipay_dict(value)
    @property
    def tenant_id(self):
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, value):
        self._tenant_id = value
    @property
    def to_paid_amount(self):
        return self._to_paid_amount

    @to_paid_amount.setter
    def to_paid_amount(self, value):
        self._to_paid_amount = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount_visible:
            if hasattr(self.amount_visible, 'to_alipay_dict'):
                params['amount_visible'] = self.amount_visible.to_alipay_dict()
            else:
                params['amount_visible'] = self.amount_visible
        if self.antgroup_account:
            if hasattr(self.antgroup_account, 'to_alipay_dict'):
                params['antgroup_account'] = self.antgroup_account.to_alipay_dict()
            else:
                params['antgroup_account'] = self.antgroup_account
        if self.bank_account:
            if hasattr(self.bank_account, 'to_alipay_dict'):
                params['bank_account'] = self.bank_account.to_alipay_dict()
            else:
                params['bank_account'] = self.bank_account
        if self.bank_branch_name:
            if hasattr(self.bank_branch_name, 'to_alipay_dict'):
                params['bank_branch_name'] = self.bank_branch_name.to_alipay_dict()
            else:
                params['bank_branch_name'] = self.bank_branch_name
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.buyer:
            if hasattr(self.buyer, 'to_alipay_dict'):
                params['buyer'] = self.buyer.to_alipay_dict()
            else:
                params['buyer'] = self.buyer
        if self.buyer_dept_code:
            if hasattr(self.buyer_dept_code, 'to_alipay_dict'):
                params['buyer_dept_code'] = self.buyer_dept_code.to_alipay_dict()
            else:
                params['buyer_dept_code'] = self.buyer_dept_code
        if self.buyer_manager:
            if hasattr(self.buyer_manager, 'to_alipay_dict'):
                params['buyer_manager'] = self.buyer_manager.to_alipay_dict()
            else:
                params['buyer_manager'] = self.buyer_manager
        if self.buyer_purchase_org_id:
            if hasattr(self.buyer_purchase_org_id, 'to_alipay_dict'):
                params['buyer_purchase_org_id'] = self.buyer_purchase_org_id.to_alipay_dict()
            else:
                params['buyer_purchase_org_id'] = self.buyer_purchase_org_id
        if self.company_code:
            if hasattr(self.company_code, 'to_alipay_dict'):
                params['company_code'] = self.company_code.to_alipay_dict()
            else:
                params['company_code'] = self.company_code
        if self.company_name:
            if hasattr(self.company_name, 'to_alipay_dict'):
                params['company_name'] = self.company_name.to_alipay_dict()
            else:
                params['company_name'] = self.company_name
        if self.config_out_dto:
            if hasattr(self.config_out_dto, 'to_alipay_dict'):
                params['config_out_dto'] = self.config_out_dto.to_alipay_dict()
            else:
                params['config_out_dto'] = self.config_out_dto
        if self.confirmed:
            if hasattr(self.confirmed, 'to_alipay_dict'):
                params['confirmed'] = self.confirmed.to_alipay_dict()
            else:
                params['confirmed'] = self.confirmed
        if self.contract_number:
            if hasattr(self.contract_number, 'to_alipay_dict'):
                params['contract_number'] = self.contract_number.to_alipay_dict()
            else:
                params['contract_number'] = self.contract_number
        if self.contract_order_send_log_dto_list:
            if isinstance(self.contract_order_send_log_dto_list, list):
                for i in range(0, len(self.contract_order_send_log_dto_list)):
                    element = self.contract_order_send_log_dto_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.contract_order_send_log_dto_list[i] = element.to_alipay_dict()
            if hasattr(self.contract_order_send_log_dto_list, 'to_alipay_dict'):
                params['contract_order_send_log_dto_list'] = self.contract_order_send_log_dto_list.to_alipay_dict()
            else:
                params['contract_order_send_log_dto_list'] = self.contract_order_send_log_dto_list
        if self.contract_type:
            if hasattr(self.contract_type, 'to_alipay_dict'):
                params['contract_type'] = self.contract_type.to_alipay_dict()
            else:
                params['contract_type'] = self.contract_type
        if self.creator:
            if hasattr(self.creator, 'to_alipay_dict'):
                params['creator'] = self.creator.to_alipay_dict()
            else:
                params['creator'] = self.creator
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.data_source:
            if hasattr(self.data_source, 'to_alipay_dict'):
                params['data_source'] = self.data_source.to_alipay_dict()
            else:
                params['data_source'] = self.data_source
        if self.demander_purchase_org_id:
            if hasattr(self.demander_purchase_org_id, 'to_alipay_dict'):
                params['demander_purchase_org_id'] = self.demander_purchase_org_id.to_alipay_dict()
            else:
                params['demander_purchase_org_id'] = self.demander_purchase_org_id
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.effect_date_range:
            if hasattr(self.effect_date_range, 'to_alipay_dict'):
                params['effect_date_range'] = self.effect_date_range.to_alipay_dict()
            else:
                params['effect_date_range'] = self.effect_date_range
        if self.effect_date_range_end:
            if hasattr(self.effect_date_range_end, 'to_alipay_dict'):
                params['effect_date_range_end'] = self.effect_date_range_end.to_alipay_dict()
            else:
                params['effect_date_range_end'] = self.effect_date_range_end
        if self.effect_date_range_start:
            if hasattr(self.effect_date_range_start, 'to_alipay_dict'):
                params['effect_date_range_start'] = self.effect_date_range_start.to_alipay_dict()
            else:
                params['effect_date_range_start'] = self.effect_date_range_start
        if self.effect_time:
            if hasattr(self.effect_time, 'to_alipay_dict'):
                params['effect_time'] = self.effect_time.to_alipay_dict()
            else:
                params['effect_time'] = self.effect_time
        if self.email_status:
            if hasattr(self.email_status, 'to_alipay_dict'):
                params['email_status'] = self.email_status.to_alipay_dict()
            else:
                params['email_status'] = self.email_status
        if self.exchange_rate:
            if hasattr(self.exchange_rate, 'to_alipay_dict'):
                params['exchange_rate'] = self.exchange_rate.to_alipay_dict()
            else:
                params['exchange_rate'] = self.exchange_rate
        if self.external_po_number:
            if hasattr(self.external_po_number, 'to_alipay_dict'):
                params['external_po_number'] = self.external_po_number.to_alipay_dict()
            else:
                params['external_po_number'] = self.external_po_number
        if self.file_list:
            if isinstance(self.file_list, list):
                for i in range(0, len(self.file_list)):
                    element = self.file_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.file_list[i] = element.to_alipay_dict()
            if hasattr(self.file_list, 'to_alipay_dict'):
                params['file_list'] = self.file_list.to_alipay_dict()
            else:
                params['file_list'] = self.file_list
        if self.files:
            if hasattr(self.files, 'to_alipay_dict'):
                params['files'] = self.files.to_alipay_dict()
            else:
                params['files'] = self.files
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.has_electronic_sign:
            if hasattr(self.has_electronic_sign, 'to_alipay_dict'):
                params['has_electronic_sign'] = self.has_electronic_sign.to_alipay_dict()
            else:
                params['has_electronic_sign'] = self.has_electronic_sign
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.invoiced_amount:
            if hasattr(self.invoiced_amount, 'to_alipay_dict'):
                params['invoiced_amount'] = self.invoiced_amount.to_alipay_dict()
            else:
                params['invoiced_amount'] = self.invoiced_amount
        if self.is_ant_group:
            if hasattr(self.is_ant_group, 'to_alipay_dict'):
                params['is_ant_group'] = self.is_ant_group.to_alipay_dict()
            else:
                params['is_ant_group'] = self.is_ant_group
        if self.is_cash_pay:
            if hasattr(self.is_cash_pay, 'to_alipay_dict'):
                params['is_cash_pay'] = self.is_cash_pay.to_alipay_dict()
            else:
                params['is_cash_pay'] = self.is_cash_pay
        if self.is_cheque_pay:
            if hasattr(self.is_cheque_pay, 'to_alipay_dict'):
                params['is_cheque_pay'] = self.is_cheque_pay.to_alipay_dict()
            else:
                params['is_cheque_pay'] = self.is_cheque_pay
        if self.is_delivery_detail:
            if hasattr(self.is_delivery_detail, 'to_alipay_dict'):
                params['is_delivery_detail'] = self.is_delivery_detail.to_alipay_dict()
            else:
                params['is_delivery_detail'] = self.is_delivery_detail
        if self.is_expire_remind:
            if hasattr(self.is_expire_remind, 'to_alipay_dict'):
                params['is_expire_remind'] = self.is_expire_remind.to_alipay_dict()
            else:
                params['is_expire_remind'] = self.is_expire_remind
        if self.item_list:
            if isinstance(self.item_list, list):
                for i in range(0, len(self.item_list)):
                    element = self.item_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_list[i] = element.to_alipay_dict()
            if hasattr(self.item_list, 'to_alipay_dict'):
                params['item_list'] = self.item_list.to_alipay_dict()
            else:
                params['item_list'] = self.item_list
        if self.modifier:
            if hasattr(self.modifier, 'to_alipay_dict'):
                params['modifier'] = self.modifier.to_alipay_dict()
            else:
                params['modifier'] = self.modifier
        if self.no_contract_reason:
            if hasattr(self.no_contract_reason, 'to_alipay_dict'):
                params['no_contract_reason'] = self.no_contract_reason.to_alipay_dict()
            else:
                params['no_contract_reason'] = self.no_contract_reason
        if self.order_channel:
            if hasattr(self.order_channel, 'to_alipay_dict'):
                params['order_channel'] = self.order_channel.to_alipay_dict()
            else:
                params['order_channel'] = self.order_channel
        if self.origin_currency:
            if hasattr(self.origin_currency, 'to_alipay_dict'):
                params['origin_currency'] = self.origin_currency.to_alipay_dict()
            else:
                params['origin_currency'] = self.origin_currency
        if self.ou_code:
            if hasattr(self.ou_code, 'to_alipay_dict'):
                params['ou_code'] = self.ou_code.to_alipay_dict()
            else:
                params['ou_code'] = self.ou_code
        if self.paid_amount:
            if hasattr(self.paid_amount, 'to_alipay_dict'):
                params['paid_amount'] = self.paid_amount.to_alipay_dict()
            else:
                params['paid_amount'] = self.paid_amount
        if self.payee_account_name:
            if hasattr(self.payee_account_name, 'to_alipay_dict'):
                params['payee_account_name'] = self.payee_account_name.to_alipay_dict()
            else:
                params['payee_account_name'] = self.payee_account_name
        if self.payee_bank_id:
            if hasattr(self.payee_bank_id, 'to_alipay_dict'):
                params['payee_bank_id'] = self.payee_bank_id.to_alipay_dict()
            else:
                params['payee_bank_id'] = self.payee_bank_id
        if self.payee_id:
            if hasattr(self.payee_id, 'to_alipay_dict'):
                params['payee_id'] = self.payee_id.to_alipay_dict()
            else:
                params['payee_id'] = self.payee_id
        if self.payee_name:
            if hasattr(self.payee_name, 'to_alipay_dict'):
                params['payee_name'] = self.payee_name.to_alipay_dict()
            else:
                params['payee_name'] = self.payee_name
        if self.payment_plan_dto:
            if hasattr(self.payment_plan_dto, 'to_alipay_dict'):
                params['payment_plan_dto'] = self.payment_plan_dto.to_alipay_dict()
            else:
                params['payment_plan_dto'] = self.payment_plan_dto
        if self.po_billable_info_dto:
            if hasattr(self.po_billable_info_dto, 'to_alipay_dict'):
                params['po_billable_info_dto'] = self.po_billable_info_dto.to_alipay_dict()
            else:
                params['po_billable_info_dto'] = self.po_billable_info_dto
        if self.po_number:
            if hasattr(self.po_number, 'to_alipay_dict'):
                params['po_number'] = self.po_number.to_alipay_dict()
            else:
                params['po_number'] = self.po_number
        if self.quotation_approved_time:
            if hasattr(self.quotation_approved_time, 'to_alipay_dict'):
                params['quotation_approved_time'] = self.quotation_approved_time.to_alipay_dict()
            else:
                params['quotation_approved_time'] = self.quotation_approved_time
        if self.quotation_number:
            if hasattr(self.quotation_number, 'to_alipay_dict'):
                params['quotation_number'] = self.quotation_number.to_alipay_dict()
            else:
                params['quotation_number'] = self.quotation_number
        if self.reusable_contract_code:
            if hasattr(self.reusable_contract_code, 'to_alipay_dict'):
                params['reusable_contract_code'] = self.reusable_contract_code.to_alipay_dict()
            else:
                params['reusable_contract_code'] = self.reusable_contract_code
        if self.source_type:
            if hasattr(self.source_type, 'to_alipay_dict'):
                params['source_type'] = self.source_type.to_alipay_dict()
            else:
                params['source_type'] = self.source_type
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.structured_detail_biz_scene:
            if hasattr(self.structured_detail_biz_scene, 'to_alipay_dict'):
                params['structured_detail_biz_scene'] = self.structured_detail_biz_scene.to_alipay_dict()
            else:
                params['structured_detail_biz_scene'] = self.structured_detail_biz_scene
        if self.supplier_id:
            if hasattr(self.supplier_id, 'to_alipay_dict'):
                params['supplier_id'] = self.supplier_id.to_alipay_dict()
            else:
                params['supplier_id'] = self.supplier_id
        if self.supplier_link:
            if hasattr(self.supplier_link, 'to_alipay_dict'):
                params['supplier_link'] = self.supplier_link.to_alipay_dict()
            else:
                params['supplier_link'] = self.supplier_link
        if self.tenant_id:
            if hasattr(self.tenant_id, 'to_alipay_dict'):
                params['tenant_id'] = self.tenant_id.to_alipay_dict()
            else:
                params['tenant_id'] = self.tenant_id
        if self.to_paid_amount:
            if hasattr(self.to_paid_amount, 'to_alipay_dict'):
                params['to_paid_amount'] = self.to_paid_amount.to_alipay_dict()
            else:
                params['to_paid_amount'] = self.to_paid_amount
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PurchaseOrderOutDTO()
        if 'amount_visible' in d:
            o.amount_visible = d['amount_visible']
        if 'antgroup_account' in d:
            o.antgroup_account = d['antgroup_account']
        if 'bank_account' in d:
            o.bank_account = d['bank_account']
        if 'bank_branch_name' in d:
            o.bank_branch_name = d['bank_branch_name']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'buyer' in d:
            o.buyer = d['buyer']
        if 'buyer_dept_code' in d:
            o.buyer_dept_code = d['buyer_dept_code']
        if 'buyer_manager' in d:
            o.buyer_manager = d['buyer_manager']
        if 'buyer_purchase_org_id' in d:
            o.buyer_purchase_org_id = d['buyer_purchase_org_id']
        if 'company_code' in d:
            o.company_code = d['company_code']
        if 'company_name' in d:
            o.company_name = d['company_name']
        if 'config_out_dto' in d:
            o.config_out_dto = d['config_out_dto']
        if 'confirmed' in d:
            o.confirmed = d['confirmed']
        if 'contract_number' in d:
            o.contract_number = d['contract_number']
        if 'contract_order_send_log_dto_list' in d:
            o.contract_order_send_log_dto_list = d['contract_order_send_log_dto_list']
        if 'contract_type' in d:
            o.contract_type = d['contract_type']
        if 'creator' in d:
            o.creator = d['creator']
        if 'currency' in d:
            o.currency = d['currency']
        if 'data_source' in d:
            o.data_source = d['data_source']
        if 'demander_purchase_org_id' in d:
            o.demander_purchase_org_id = d['demander_purchase_org_id']
        if 'description' in d:
            o.description = d['description']
        if 'effect_date_range' in d:
            o.effect_date_range = d['effect_date_range']
        if 'effect_date_range_end' in d:
            o.effect_date_range_end = d['effect_date_range_end']
        if 'effect_date_range_start' in d:
            o.effect_date_range_start = d['effect_date_range_start']
        if 'effect_time' in d:
            o.effect_time = d['effect_time']
        if 'email_status' in d:
            o.email_status = d['email_status']
        if 'exchange_rate' in d:
            o.exchange_rate = d['exchange_rate']
        if 'external_po_number' in d:
            o.external_po_number = d['external_po_number']
        if 'file_list' in d:
            o.file_list = d['file_list']
        if 'files' in d:
            o.files = d['files']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'has_electronic_sign' in d:
            o.has_electronic_sign = d['has_electronic_sign']
        if 'id' in d:
            o.id = d['id']
        if 'invoiced_amount' in d:
            o.invoiced_amount = d['invoiced_amount']
        if 'is_ant_group' in d:
            o.is_ant_group = d['is_ant_group']
        if 'is_cash_pay' in d:
            o.is_cash_pay = d['is_cash_pay']
        if 'is_cheque_pay' in d:
            o.is_cheque_pay = d['is_cheque_pay']
        if 'is_delivery_detail' in d:
            o.is_delivery_detail = d['is_delivery_detail']
        if 'is_expire_remind' in d:
            o.is_expire_remind = d['is_expire_remind']
        if 'item_list' in d:
            o.item_list = d['item_list']
        if 'modifier' in d:
            o.modifier = d['modifier']
        if 'no_contract_reason' in d:
            o.no_contract_reason = d['no_contract_reason']
        if 'order_channel' in d:
            o.order_channel = d['order_channel']
        if 'origin_currency' in d:
            o.origin_currency = d['origin_currency']
        if 'ou_code' in d:
            o.ou_code = d['ou_code']
        if 'paid_amount' in d:
            o.paid_amount = d['paid_amount']
        if 'payee_account_name' in d:
            o.payee_account_name = d['payee_account_name']
        if 'payee_bank_id' in d:
            o.payee_bank_id = d['payee_bank_id']
        if 'payee_id' in d:
            o.payee_id = d['payee_id']
        if 'payee_name' in d:
            o.payee_name = d['payee_name']
        if 'payment_plan_dto' in d:
            o.payment_plan_dto = d['payment_plan_dto']
        if 'po_billable_info_dto' in d:
            o.po_billable_info_dto = d['po_billable_info_dto']
        if 'po_number' in d:
            o.po_number = d['po_number']
        if 'quotation_approved_time' in d:
            o.quotation_approved_time = d['quotation_approved_time']
        if 'quotation_number' in d:
            o.quotation_number = d['quotation_number']
        if 'reusable_contract_code' in d:
            o.reusable_contract_code = d['reusable_contract_code']
        if 'source_type' in d:
            o.source_type = d['source_type']
        if 'status' in d:
            o.status = d['status']
        if 'structured_detail_biz_scene' in d:
            o.structured_detail_biz_scene = d['structured_detail_biz_scene']
        if 'supplier_id' in d:
            o.supplier_id = d['supplier_id']
        if 'supplier_link' in d:
            o.supplier_link = d['supplier_link']
        if 'tenant_id' in d:
            o.tenant_id = d['tenant_id']
        if 'to_paid_amount' in d:
            o.to_paid_amount = d['to_paid_amount']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        return o


