use Monitoramento

create table Torno (
	timestamp datetime not null DEFAULT current_timestamp,
	gas float,
	temperature float,
	rpm int,
	nivel bit,
	giro bit,
	stat bit
);

insert into Torno(gas, temperature, rpm, nivel, giro, stat) values 
	(1.2, 21.5, 1000, 1, 0, 1)

select * from Torno