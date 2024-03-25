from sqlalchemy import CHAR, Column, DECIMAL, Date, DateTime, Enum, ForeignKey, Index, String, TIMESTAMP, Text, text
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, MEDIUMTEXT, TIMESTAMP, TINYINT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()

class AddressModel(Base):
    __tablename__ = 'address'

    address_pk = Column(INTEGER(11), primary_key=True)
    street = Column(String(1000))
    house_number = Column(String(255))
    zip_code = Column(String(255))
    city = Column(String(255))
    country = Column(String(255))


class ChargingProfileModel(Base):
    __tablename__ = 'charging_profile'

    charging_profile_pk = Column(INTEGER(11), primary_key=True)
    stack_level = Column(INTEGER(11), nullable=False)
    charging_profile_purpose = Column(String(255), nullable=False)
    charging_profile_kind = Column(String(255), nullable=False)
    recurrency_kind = Column(String(255))
    valid_from = Column(TIMESTAMP(fsp=6))
    valid_to = Column(TIMESTAMP(fsp=6))
    duration_in_seconds = Column(INTEGER(11))
    start_schedule = Column(TIMESTAMP(fsp=6))
    charging_rate_unit = Column(String(255), nullable=False)
    min_charging_rate = Column(DECIMAL(15, 1))
    description = Column(String(255))
    note = Column(Text)

    # connector = relationship('Connector', secondary='connector_charging_profile')
    # charging_schedule_periods = relationship("ChargingSchedulePeriod", back_populates="charging_profile")


class OcppTagModel(Base):
    __tablename__ = 'ocpp_tag'

    ocpp_tag_pk = Column(INTEGER(11), primary_key=True)
    id_tag = Column(String(255), nullable=False, unique=True)
    parent_id_tag = Column(ForeignKey('ocpp_tag.id_tag'), index=True, nullable=True)
    expiry_date = Column(TIMESTAMP(fsp=6), index=True, nullable=True)
    max_active_transaction_count = Column(INTEGER(11), nullable=False, server_default=text("1"))
    note = Column(MEDIUMTEXT, nullable=True)

    # parent = relationship('OcppTag', remote_side=[id_tag])

    def __repr__(self) -> str:
        return f"{self.id_tag}"
    


class OcppTagActivityModel(Base):
    __tablename__ = 'ocpp_tag_activity'

    ocpp_tag_pk = Column(INTEGER(11), primary_key=True, server_default=text("'0'"))
    id_tag = Column(String(255))
    parent_id_tag = Column(String(255))
    expiry_date = Column(TIMESTAMP(fsp=6))
    max_active_transaction_count = Column(INTEGER(11), server_default=text("'1'"))
    note = Column(MEDIUMTEXT)
    active_transaction_count = Column(BIGINT(21))
    in_transaction = Column(INTEGER(1))
    blocked = Column(INTEGER(1), server_default=text("'0'"))


class SchemaVersionModel(Base):
    __tablename__ = 'schema_version'

    installed_rank = Column(INTEGER(11), primary_key=True)
    version = Column(String(50))
    description = Column(String(200), nullable=False)
    type = Column(String(20), nullable=False)
    script = Column(String(1000), nullable=False)
    checksum = Column(INTEGER(11))
    installed_by = Column(String(100), nullable=False)
    installed_on = Column(TIMESTAMP, nullable=False, server_default=text("current_timestamp()"))
    execution_time = Column(INTEGER(11), nullable=False)
    success = Column(TINYINT(1), nullable=False, index=True)


class SettingModel(Base):
    __tablename__ = 'settings'

    app_id = Column(String(40), primary_key=True, unique=True)
    heartbeat_interval_in_seconds = Column(INTEGER(11))
    hours_to_expire = Column(INTEGER(11))
    mail_enabled = Column(TINYINT(1), server_default=text("0"))
    mail_host = Column(String(255))
    mail_username = Column(String(255))
    mail_password = Column(String(255))
    mail_from = Column(String(255))
    mail_protocol = Column(String(255), server_default=text("'smtp'"))
    mail_port = Column(INTEGER(11), server_default=text("25"))
    mail_recipients = Column(Text, comment='comma separated list of email addresses')
    notification_features = Column(Text, comment='comma separated list')


class TransactionModel(Base):
    __tablename__ = 'transaction'

    transaction_pk = Column(INTEGER(10), primary_key=True, server_default=text("'0'"))
    connector_pk = Column(INTEGER(10))
    id_tag = Column(String(255))
    start_event_timestamp = Column(TIMESTAMP(fsp=6), server_default=text("current_timestamp(6)"))
    start_timestamp = Column(TIMESTAMP(fsp=6))
    start_value = Column(String(255))
    stop_event_actor = Column(Enum('station', 'manual'))
    stop_event_timestamp = Column(TIMESTAMP(fsp=6), server_default=text("current_timestamp(6)"))
    stop_timestamp = Column(TIMESTAMP(fsp=6), server_default=text("current_timestamp(6)"))
    stop_value = Column(String(255))
    stop_reason = Column(String(255))

    def __repr__(self) -> str:
        return f"{self.transaction_pk}-{self.id_tag}-{self.start_timestamp}-to-{self.stop_timestamp}"


class TransactionStopFailedModel(Base):
    __tablename__ = 'transaction_stop_failed'

    transaction_pk = Column(INTEGER(11), primary_key=True)
    event_timestamp = Column(TIMESTAMP(fsp=6), nullable=False, server_default=text("current_timestamp(6)"))
    event_actor = Column(Enum('station', 'manual'))
    stop_timestamp = Column(TIMESTAMP(fsp=6), nullable=False, server_default=text("current_timestamp(6)"))
    stop_value = Column(String(255))
    stop_reason = Column(String(255))
    fail_reason = Column(Text)


class ChargeBoxModel(Base):
    __tablename__ = 'charge_box'
    __table_args__ = (Index('chargebox_op_ep_idx', 'ocpp_protocol', 'endpoint_address'), )

    charge_box_pk = Column(INTEGER(11), primary_key=True)
    charge_box_id = Column(String(255), nullable=False, unique=True)
    endpoint_address = Column(String(255))
    ocpp_protocol = Column(String(255))
    registration_status = Column(String(255), nullable=False, server_default=text("'Accepted'"))
    charge_point_vendor = Column(String(255))
    charge_point_model = Column(String(255))
    charge_point_serial_number = Column(String(255))
    charge_box_serial_number = Column(String(255))
    fw_version = Column(String(255))
    fw_update_status = Column(String(255))
    fw_update_timestamp = Column(TIMESTAMP(fsp=6))
    iccid = Column(String(255))
    imsi = Column(String(255))
    meter_type = Column(String(255))
    meter_serial_number = Column(String(255))
    diagnostics_status = Column(String(255))
    diagnostics_timestamp = Column(TIMESTAMP(fsp=6))
    last_heartbeat_timestamp = Column(TIMESTAMP(fsp=6))
    description = Column(MEDIUMTEXT)
    note = Column(MEDIUMTEXT)
    location_latitude = Column(DECIMAL(11, 8))
    location_longitude = Column(DECIMAL(11, 8))
    address_pk = Column(ForeignKey('address.address_pk', ondelete='SET NULL'), index=True)
    admin_address = Column(String(255))
    insert_connector_status_after_transaction_msg = Column(TINYINT(1), server_default=text("1"))

    connectors = relationship("ConnectorModel", back_populates="charge_box", lazy="immediate")

    def __repr__(self) -> str:
        return f"{self.charge_box_id}"
    
    @property
    def connector_id_to_pk_dict(self) -> dict:
        connectors_dict = {}
        for connector in self.connectors:
            connectors_dict[connector.connector_id] = connector.connector_pk
        return connectors_dict
    
    @property
    def total_connectors(self) -> int:
        return len(self.connectors)


class ChargingSchedulePeriodModel(Base):
    __tablename__ = 'charging_schedule_period'
    __table_args__ = (Index('UQ_charging_schedule_period', 'charging_profile_pk', 'start_period_in_seconds', unique=True), )

    charging_profile_pk = Column(INTEGER, ForeignKey('charging_profile.charging_profile_pk', ondelete='CASCADE'), primary_key=True, nullable=False)
    start_period_in_seconds = Column(INTEGER(11), primary_key=True, nullable=False)
    power_limit = Column(DECIMAL(15, 1), nullable=False)
    number_phases = Column(INTEGER(11))
    
    # charging_profile = relationship("ChargingProfile", back_populates="charging_schedule_periods")


class UserModel(Base):
    __tablename__ = 'user'

    user_pk = Column(INTEGER(11), primary_key=True)
    ocpp_tag_pk = Column(ForeignKey('ocpp_tag.ocpp_tag_pk', ondelete='SET NULL'), index=True)
    address_pk = Column(ForeignKey('address.address_pk', ondelete='SET NULL'), index=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    birth_day = Column(Date)
    sex = Column(CHAR(1))
    phone = Column(String(255))
    e_mail = Column(String(255))
    note = Column(MEDIUMTEXT)
    
    # address = relationship('Address')
    # ocpp_tag = relationship('OcppTag')


class ConnectorModel(Base):
    __tablename__ = 'connector'
    __table_args__ = (Index('connector_cbid_cid_UNIQUE', 'charge_box_id', 'connector_id', unique=True), )

    connector_pk = Column(INTEGER(11), primary_key=True, unique=True)
    charge_box_id = Column(ForeignKey('charge_box.charge_box_id', ondelete='CASCADE'), nullable=False)
    connector_id = Column(INTEGER(11), nullable=False)

    charge_box = relationship("ChargeBoxModel", back_populates="connectors")


    def __repr__(self) -> str:
        return f"connector_{self.connector_id}"
    

   
    
    # charge_box = relationship('ChargeBox')
    # charging_profiles = relationship('ChargingProfile', secondary='charging_profile_connector')
    # charging_profile_connector = relationship('ChargingProfile', secondary='charging_profile_connector')


class ConnectorChargingProfileModel(Base):
    __tablename__ = 'connector_charging_profile'
    __table_args__ = (Index('UQ_connector_charging_profile', 'connector_pk', 'charging_profile_pk', unique=True), )

    connector_pk = Column(INTEGER, ForeignKey('connector.connector_pk', ondelete='CASCADE'), primary_key=True, nullable=False)
    charging_profile_pk = Column(INTEGER, ForeignKey('charging_profile.charging_profile_pk'), primary_key=True, nullable=False, index=True)
    
    #connector = relationship("Connector", back_populates="charging_profiles")

    def __repr__(self) -> str:
        return f"{self.charging_profile_pk}"
    

class ConnectorStatusModel(Base):
    __tablename__ = 'connector_status'
    __table_args__ = (Index('connector_status_cpk_st_idx', 'connector_pk', 'status_timestamp'), )

    connector_pk = Column(INTEGER, ForeignKey('connector.connector_pk', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
    status_timestamp = Column(TIMESTAMP(fsp=6))
    status = Column(String(255))
    error_code = Column(String(255))
    error_info = Column(String(255))
    vendor_id = Column(String(255))
    vendor_error_code = Column(String(255))

    def __repr__(self) -> str:
        return f"{self.connector_pk}"


class TransactionStartModel(Base):
    __tablename__ = 'transaction_start'

    transaction_pk = Column(INTEGER(10), primary_key=True, unique=True)
    event_timestamp = Column(TIMESTAMP(fsp=6), nullable=False, server_default=text("current_timestamp(6)"))
    connector_pk = Column(ForeignKey('connector.connector_pk', ondelete='CASCADE'), nullable=False, index=True)
    id_tag = Column(ForeignKey('ocpp_tag.id_tag', ondelete='CASCADE'), nullable=False, index=True)
    start_timestamp = Column(TIMESTAMP(fsp=6), index=True)
    start_value = Column(String(255))

    # connector = relationship('Connector')
    # ocpp_tag = relationship('OcppTag')


class ConnectorMeterValueModel(Base):
    __tablename__ = 'connector_meter_value'
    __table_args__ = (Index('connector_meter_value_idx', 'connector_pk', 'value_timestamp'), )

    connector_pk = Column(INTEGER, ForeignKey('connector.connector_pk', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
    transaction_pk = Column(INTEGER, ForeignKey('transaction_start.transaction_pk', ondelete='SET NULL'), index=True)
    value_timestamp = Column(TIMESTAMP(fsp=6), index=True)
    value = Column(Text)
    reading_context = Column(String(255))
    format = Column(String(255))
    measurand = Column(String(255))
    location = Column(String(255))
    unit = Column(String(255))
    phase = Column(String(255))

    # connector = relationship("Connector", back_populates="meter_values")
    # transaction = relationship("TransactionStart")  # Assuming there's a TransactionStart class


class ReservationModel(Base):
    __tablename__ = 'reservation'

    reservation_pk = Column(INTEGER(10), primary_key=True, unique=True)
    connector_pk = Column(ForeignKey('connector.connector_pk', ondelete='CASCADE'), nullable=False, index=True)
    transaction_pk = Column(ForeignKey('transaction_start.transaction_pk'), unique=True)
    id_tag = Column(ForeignKey('ocpp_tag.id_tag', ondelete='CASCADE'), nullable=False, index=True)
    start_datetime = Column(DateTime, index=True)
    expiry_datetime = Column(DateTime, index=True)
    status = Column(String(255), nullable=False, index=True)

    # connector = relationship('Connector')
    # ocpp_tag = relationship('OcppTag')
    # transaction_start = relationship('TransactionStart')


class TransactionStopModel(Base):
    __tablename__ = 'transaction_stop'

    transaction_pk = Column(ForeignKey('transaction_start.transaction_pk', ondelete='CASCADE'), primary_key=True, nullable=False)
    event_timestamp = Column(TIMESTAMP(fsp=6), primary_key=True, nullable=False, server_default=text("current_timestamp(6)"))
    event_actor = Column(Enum('station', 'manual'))
    stop_timestamp = Column(TIMESTAMP(fsp=6), nullable=False, server_default=text("current_timestamp(6)"))
    stop_value = Column(String(255), nullable=False)
    stop_reason = Column(String(255))

    # transaction_start = relationship('TransactionStart')
